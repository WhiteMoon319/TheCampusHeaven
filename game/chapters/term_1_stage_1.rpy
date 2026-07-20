label stage_1_intro:

    window hide
    centered "一年后的中考，\n你超常发挥，拿下了736的高分，\n顺利进入了离你家很近的重庆八中渝北校区。\n虽然你的身高还是定格在了143cm，\n但至少八中没有人会欺负你。"
    window auto
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
    "[player_name]"
    "庄...庄桂清？"
    zhuang "嗯？你是...？"
    "[player_name]"
    "你不记得我了吗...初二那年，在厕所里..."
    zhuang "是你！你后来去哪了？我一直想知道你的名字。"
    "[player_name]"
    "我叫[player_name]。"
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
