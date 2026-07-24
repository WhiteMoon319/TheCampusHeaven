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

    sdk_dir = os.path.abspath(args.sdk_dir)
    rapt_dir = os.path.join(sdk_dir, "rapt")
    build_dir = os.path.join(sdk_dir, "build_dir")

    sys.path.insert(0, os.path.join(rapt_dir, "buildlib"))
    sys.path.insert(0, sdk_dir)

    import rapt.interface

    rapt.interface.Style = type("Style", (), {"BRIGHT": ""})
    import rapt.build
    import rapt.configure

    iface = rapt.interface.Interface()

    os.chdir(rapt_dir)

    anydpi_dir = os.path.join(
        "prototype", "app", "src", "main", "res", "mipmap-anydpi-v26"
    )
    os.makedirs(anydpi_dir, exist_ok=True)

    adaptive_icon_xml = (
        '<?xml version="1.0" encoding="utf-8"?>\n'
        '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
        '    <background android:drawable="@mipmap/icon_background"/>\n'
        '    <foreground android:drawable="@mipmap/icon_foreground"/>\n'
        '</adaptive-icon>\n'
    )

    for xml_name in ("icon.xml", "icon_round.xml"):
        with open(os.path.join(anydpi_dir, xml_name), "w", encoding="utf-8") as f:
            f.write(adaptive_icon_xml)

    manifest_template = os.path.join("templates", "app-AndroidManifest.xml")
    with open(manifest_template, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace(
        'android:icon="@mipmap/icon"',
        'android:icon="@mipmap/icon"\n      android:roundIcon="@mipmap/icon_round"',
    )
    with open(manifest_template, "w", encoding="utf-8") as f:
        f.write(content)

    rapt.build.copy_project()

    answers = "\n".join([
        args.name,
        "",
        args.package,
        "5",
        "1",
        "4",
        "1",
        args.ks_alias,
        args.ks_pass,
        args.key_pass,
        "",
        "",
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

    import shutil as _shutil

    workspace = os.path.abspath(args.workspace)
    for fn in os.listdir(workspace):
        if fn.startswith("android-"):
            src = os.path.join(workspace, fn)
            dst = os.path.join(build_dir, fn)
            if os.path.isfile(src) and not os.path.exists(dst):
                _shutil.copy2(src, dst)

    game_dir = os.path.join(build_dir, "game")
    if os.path.isdir(game_dir):
        for fn in os.listdir(game_dir):
            if fn.startswith("android-"):
                src = os.path.join(game_dir, fn)
                dst = os.path.join(build_dir, fn)
                if not os.path.exists(dst):
                    _shutil.copy2(src, dst)

    rapt.build.build(iface, directory=build_dir, base=args.workspace)


if __name__ == "__main__":
    main()
