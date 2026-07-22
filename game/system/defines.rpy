# 由 excel_to_rpy.py 定义管理器自动生成


# ========================================
# 小男孩（boy）
# ========================================

define boy = Character("小男孩")
image boy_block = Solid("#f39c12", xsize=200, ysize=350)


# ========================================
# 陈叙塬（chen）
# ========================================

define chen = Character("陈叙塬")
default attune_chen = 0
default guard_chen = 100
default score_chen = 0


# ========================================
# 陆明远（lu）
# ========================================

define lu = Character("陆明远")
default admire_lu = 25
default score_lu = 0
default tenderness_lu = 0
image lu_block = Solid("#9b59b6", xsize=250, ysize=450)


# ========================================
# 叙述者（narrator）
# ========================================

define narrator = Character("")


# ========================================
# 学生A（student_a）
# ========================================

define student_a = Character("学生A")


# ========================================
# 学生B（student_b）
# ========================================

define student_b = Character("学生B")


# ========================================
# 徐忍（xur）
# ========================================

define xur = Character("徐忍")


# ========================================
# 庄桂清（zhuang）
# ========================================

define zhuang = Character("庄桂清")
default love_zhuang = 0
default score_zhuang = 0
default trust_zhuang = 0
image zhuang_block = Solid("#50c878", xsize=250, ysize=450)


# ========================================
# 玩家
# ========================================

default player_name = ""
image player_block = Solid("#4a90d9", xsize=250, ysize=450)


# ========================================
# 背景
# ========================================

image bg classroom = Transform("images/background/Classroom.jpg", size=(1920, 1080))
image bg room_zhuang = Transform("images/background/Room_zhuang.jpg", size=(1920, 1080))
image bg school = Transform("images/background/School.jpg", size=(1920, 1080))
image bg toilet = Transform("images/background/Toliet.png", size=(1920, 1080))


# ========================================
# 系统/全局定义
# ========================================

default score = 0
image student_block = Solid("#e74c3c", xsize=250, ysize=450)

