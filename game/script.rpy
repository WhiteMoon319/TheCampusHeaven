define narrator = Character("")
define student_a = Character("学生A")
define student_b = Character("学生B")
define boy = Character("小男孩")
define zhuang = Character("庄桂清")
define lu = Character("陆明远")

default player_name = ""

image bg toilet = Transform("images/background/Toliet.png", size=(1920, 1080))
image bg school = Transform("images/background/School.jpg", size=(1920, 1080))
image bg classroom = Transform("images/background/Classroom.jpg", size=(1920, 1080))
image bg room_zhuang = Transform("images/background/Room_zhuang.jpg", size=(1920, 1080))

image player_block = Solid("#4a90d9", xsize=250, ysize=450)
image zhuang_block = Solid("#50c878", xsize=250, ysize=450)
image bully_block = Solid("#e74c3c", xsize=250, ysize=450)
image boy_block = Solid("#f39c12", xsize=200, ysize=350)
image lu_block = Solid("#9b59b6", xsize=250, ysize=450)

label start:

    $ preferences.text_cps = 40

    stop music fadeout 1.0

    scene bg toilet with fade
    show bully_block at center
    show bully_block as bully2 at right

    narrator "一阵又一阵的骚乱声中，你被推到了地上..."
    narrator "你抬头望去，三个凶神恶煞的高年级学生挡在了你的面前。"

    student_a "小不点？怎么都初二了还这么矮啊？你爸妈没给你吃饭啊？"

    narrator "你看见三个人围了上来，对着你拳打脚踢，又说又笑。"
    narrator "你躺在角落里瑟瑟发抖，不断抽泣着。"

    "此时，一个看着比你大了很多的小男孩突然闯了进来，他举着手机，高声大呼"

    show boy_block at left with moveinleft

    boy "我...我已经告诉老师了！...你们等着处分吧！"

    narrator "虽然他的语气中带着一些颤抖，但你却看见了他眼中的那抹光。"

    "那几个高年级学生站起来互相对视了一眼"

    student_b "小兔崽子，别让我逮到你。"

    hide bully_block
    hide bully2

    narrator "为首的那个，带着其他两个人离开了厕所。"

    show boy_block at center with move

    "你看见那个小男孩朝你走来，蹲下身，向你伸出手。"

    zhuang "你好啊，我叫庄桂清..."

    scene black
    window hide
    centered "从此，\n你认识了这个叫庄桂清的人，\n但你们的交集，\n却好像只局限在了这一次见面。\n而你...\n甚至没能告诉他你的名字..."
    window auto

    python:
        player_name = renpy.input("请输入你的名字：", length=12).strip()
        if player_name == "":
            player_name = "小不点"

    window hide
    centered "一年后的中考，\n你超常发挥，拿下了736的高分，\n顺利进入了离你家很近的重庆八中渝北校区。\n虽然你的身高还是定格在了143cm，\n但至少八中没有人会欺负你。"
    window auto

    scene bg school with dissolve

    scene black
    window hide
    centered "高一时，你远远望见一个熟悉的身影。\n你知道，他就是庄桂清。\n后来，你找了自己的表叔——徐忍，\n在高一下分班的时候，把你和庄桂清分到了一个班..."
    window auto

    window hide
    centered "{size=+20}高二下期...{/size}"
    window auto

    scene bg classroom with dissolve
    show player_block at left

    "你远远守候了他一年，"
    "始终不敢靠近。"

    "但是现在呢？[player_name]？"
    "在他和陈叙塬冷战的时候..."

    menu:
        "上前和他打招呼":
            jump zhuang_chen_route
        "继续守望":
            jump bad_end
        "埋头学习（陆明远线 暂未开放）":
            jump lu_mingyuan_route


label zhuang_chen_route:

    scene bg classroom with dissolve
    show player_block at left
    show zhuang_block at right with dissolve

    narrator "你深吸一口气，终于鼓起勇气走向了庄桂清。"

    "[player_name]" "庄...庄桂清？"

    zhuang "嗯？你是...？"

    "[player_name]" "你不记得我了吗...初二那年，在厕所里..."

    zhuang "是你！你后来去哪了？我一直想知道你的名字。"

    "[player_name]" "我叫[player_name]。"

    zhuang "[player_name]...好名字。"

    zhuang "好久不见。"

    narrator "他的笑容，和你记忆中一模一样。"
    narrator "而你等了这么久，终于等到了这一刻。"

    scene black
    window hide
    centered "{size=+20}——庄桂清/陈叙塬线 开启——{/size}"
    window auto

    narrator "To be continued..."

    return


label bad_end:

    scene bg school with dissolve
    show player_block at left

    narrator "你再一次低下了头，装作什么都没看见。"

    "庄桂清和陈叙塬的冷战还在继续，"
    "而你，依然远远地看着。"

    "日复一日，年复一年。"

    "直到毕业的那天，"
    "你依然没能告诉他你的名字。"

    scene black
    window hide
    centered "{size=+20}{color=#ff0000}BAD END{/color}{/size}\n{color=#ff0000}——错过——{/color}"
    window auto

    return


label lu_mingyuan_route:

    scene bg classroom with dissolve
    show player_block at left
    show lu_block at right with dissolve

    narrator "你收回了望向庄桂清的视线。"

    scene black
    window hide
    centered "{size=+20}{color=#888}——陆明远线 暂未开放，敬请期待——{/color}{/size}"
    window auto

    return
