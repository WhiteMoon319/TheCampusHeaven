"""Build TheCampusHeaven APK using Ren'Py Rapt."""
import io
import sys
import os
import json
import glob as _glob


def main():
    import argparse

    p = argparse.ArgumentParser(description="Build TheCampusHeaven APK")
    p.add_argument("--workspace", required=True, help="GitHub workspace root")
    p.add_argument("--sdk-dir", required=True, help="Ren'Py SDK directory")
    p.add_argument("--version", required=True, help="App version string")
    p.add_argument("--version-code", required=True, type=int, help="Numeric version code")
    p.add_argument("--ks-path", required=True, help="Keystore file path")
    p.add_argument("--ks-pass", required=True, help="Keystore password")
    p.add_argument("--ks-alias", required=True, help="Keystore alias")
    p.add_argument("--key-pass", required=True, help="Key password")
    p.add_argument("--name", default="TheCampusHeaven", help="App display name")
    p.add_argument("--package", default="com.WhiteMoon319.TheCampusHeaven", help="App package name")
    p.add_argument("--orientation", default="landscape")
    args = p.parse_args()

    rapt_dir = os.path.join(args.sdk_dir, "rapt")
    build_dir = os.path.join(args.sdk_dir, "build_dir")

    sys.path.insert(0, os.path.join(rapt_dir, "buildlib"))
    sys.path.insert(0, args.sdk_dir)

    import rapt.interface

    rapt.interface.Style = type("Style", (), {"BRIGHT": ""})
    import rapt.build
    import rapt.configure

    iface = rapt.interface.Interface()

    os.chdir(rapt_dir)

    rapt.build.copy_project()

    answers = "\n".join([
        args.name,
        "",
        args.package,
        "5",
        args.version,
        str(args.version_code),
        "", "", "", "", "",
        args.ks_alias,
        args.ks_pass,
        args.key_pass,
        "", "",
    ])
    sys.stdin = io.StringIO(answers)

    rapt.configure.configure(iface, directory=build_dir)

    android_json = os.path.join(build_dir, "android.json")
    with open(android_json, "r+") as f:
        config = json.load(f)
        config["update_keystores"] = False
        config["numeric_version"] = args.version_code
        config["version"] = args.version
        f.seek(0)
        f.truncate()
        json.dump(config, f)

    os.makedirs("project", exist_ok=True)
    with open(os.path.join("project", "local.properties"), "w") as f:
        f.write(f"key.store={args.ks_path}\n")
        f.write(f"key.alias={args.ks_alias}\n")
        f.write(f"key.store.password={args.ks_pass}\n")
        f.write(f"key.alias.password={args.key_pass}\n")

    for mf in _glob.glob(
        os.path.join(build_dir, "**", "AndroidManifest.xml"), recursive=True
    ):
        with open(mf, "r") as f:
            txt = f.read()
        if "screenOrientation" not in txt:
            txt = txt.replace(
                "<activity ",
                f'<activity android:screenOrientation="{args.orientation}" ',
            )
        with open(mf, "w") as f:
            f.write(txt)

    rapt.build.build(iface, directory=build_dir, base=args.workspace)


if __name__ == "__main__":
    main()
