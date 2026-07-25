init python:
    cg_list = []

    def register_cg(name, image_path, thumbnail_path=None):
        cg_list.append({
            "name": name,
            "image": image_path,
            "thumb": thumbnail_path if thumbnail_path else image_path,
        })

    def unlock_cg(name):
        if persistent.unlocked_cgs is None:
            persistent.unlocked_cgs = set()
        persistent.unlocked_cgs.add(name)

    def is_cg_unlocked(name):
        if persistent.unlocked_cgs is None:
            return False
        return name in persistent.unlocked_cgs

    register_cg("zhuang_reach", "images/cg/zhuang_cg_1.png")

image cg zhuang_reach = Transform("images/cg/zhuang_cg_1.png", size=(1920, 1080), fit="contain")


screen cg_gallery():
    tag menu

    add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                vbox:
                    spacing 20

                    label _("CG 画廊") xalign 0.5

                    if len(cg_list) == 0:
                        text _("暂无 CG，敬请期待") xalign 0.5 yalign 0.5
                    else:
                        $ cg_rows = (len(cg_list) + 3) // 4
                        grid 4 cg_rows:
                            xalign 0.5
                            spacing 20

                            for cg in cg_list:
                                if is_cg_unlocked(cg["name"]):
                                    button:
                                        xysize (300, 169)
                                        add Transform(cg["thumb"], size=(300, 169), fit="cover")
                                        action Show("cg_viewer", cg=cg)
                                else:
                                    button:
                                        xysize (300, 169)
                                        background "#333"
                                        text _("???") xalign 0.5 yalign 0.5
                                        action NullAction()

                    null height 20

                    textbutton _("返回") action Return() xalign 0.5


screen cg_viewer(cg):
    tag menu
    modal True

    add "#000"

    add Transform(cg["image"], size=(1920, 1080), fit="contain") xalign 0.5 yalign 0.5

    textbutton _("关闭") action ShowMenu("cg_gallery") xalign 0.5 yalign 0.95
