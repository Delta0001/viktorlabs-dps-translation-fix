# Generated by Selenium IDE
from numpy import size
import pytest
from time import time
from datetime import timedelta
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException

OPERATOR_IDS = ["char_123_fang", "char_240_wyvern", "char_504_rguard", "char_192_falco", "char_208_melan", "char_281_popka", "char_209_ardign", "char_122_beagle", "char_284_spot", "char_124_kroos", "char_211_adnach", "char_507_rsnipe", "char_121_lava", "char_120_hibisc", "char_212_ansel", "char_506_rmedic", "char_210_stward", "char_505_rcast", "char_278_orchid", "char_141_nights", "char_109_fmout", "char_253_greyy", "char_328_cammou", "char_469_indigo", "char_4004_pudd", "char_235_jesica", "char_126_shotst", "char_190_clour", "char_133_mm", "char_118_yuki", "char_440_pinecn", "char_302_glaze", "char_366_acdrop", "char_198_blackd", "char_149_scave", "char_290_vigna", "char_151_myrtle", "char_452_bstalk", "char_130_doberm", "char_289_gyuki", "char_159_peacok", "char_193_frostl", "char_127_estell", "char_185_frncat", "char_301_cutter", "char_337_utage", "char_271_spikes", "char_237_gravel", "char_272_strong", "char_236_rope", "char_117_myrrh", "char_187_ccheal", "char_298_susuro", "char_181_flower", "char_385_finlpp", "char_4041_chnut", "char_199_yak", "char_150_snakek", "char_381_bubble", "char_196_sunbr", "char_260_durnar", "char_110_deepcl", "char_183_skgoat", "char_258_podego", "char_484_robrta", "char_355_ethan", "char_277_sqrrel", "char_128_plosis", "char_275_breeze", "char_115_headbr", "char_102_texas", "char_349_chiave", "char_261_sddrag", "char_496_wildmn", "char_401_elysm", "char_476_blkngt", "char_308_swire", "char_265_sophia", "char_106_franka", "char_131_flameb", "char_508_aguard", "char_155_tiger", "char_415_flint", "char_140_whitew", "char_294_ayer", "char_252_bibeak", "char_459_tachak", "char_143_ghost", "char_356_broca", "char_274_astesi", "char_333_sidero", "char_475_akafyu", "char_421_crow", "char_486_takila", "char_129_bluep", "char_204_platnm", "char_367_swllow", "char_511_asnipe", "char_365_aprl", "char_1021_kroos2", "char_219_meteo", "char_379_sesa", "char_279_excu", "char_346_aosta", "char_002_amiya", "char_405_absin", "char_411_tomimi", "char_166_skfire", "char_509_acast", "char_306_leizi", "char_344_beewax", "char_373_lionhd", "char_388_mint", "char_338_iris", "char_1011_lava2", "char_489_serum", "char_4013_kjera", "char_4040_rockr", "char_242_otter", "char_336_folivo", "char_108_silent", "char_171_bldsk", "char_345_folnic", "char_510_amedic", "char_348_ceylon", "char_436_whispr", "char_402_tuye", "char_473_mberry", "char_449_glider", "char_1024_hbisc2", "char_148_nearl", "char_226_hmau", "char_144_red", "char_243_waaifu", "char_214_kafka", "char_455_nothin", "char_107_liskam", "char_201_moeshd", "char_325_bison", "char_163_hpsts", "char_378_asbest", "char_512_aprot", "char_4025_aprot2", "char_4047_pianst", "char_457_blitz", "char_304_zebra", "char_431_ashlok", "char_422_aurora", "char_145_prove", "char_158_milu", "char_218_cuttle", "char_363_toddi", "char_4043_erato", "char_173_slchan", "char_383_snsant", "char_174_slbell", "char_254_vodfox", "char_195_glassb", "char_326_glacus", "char_433_windft", "char_101_sora", "char_4045_heidi", "char_343_tknogi", "char_4019_ncdeer", "char_492_quercu", "char_215_mantic", "char_478_kirara", "char_241_panda", "char_4036_forcer", "char_451_robin", "char_458_rfrost", "char_369_bena", "char_4016_kazema", "char_103_angel", "char_332_archet", "char_456_ash", "char_340_shwaz", "char_430_fartth", "char_113_cqbw", "char_300_phenxi", "char_197_poca", "char_391_rosmon", "char_1013_chen2", "char_112_siege", "char_222_bpipe", "char_362_saga", "char_479_sleach", "char_420_flamtl", "char_134_ifrit", "char_213_mostma", "char_180_amgoat", "char_2013_cerber", "char_2015_dusk", "char_472_pasngr", "char_426_billro", "char_377_gdglow", "char_4046_ebnhlz", "char_206_gnosis", "char_291_aglina", "char_358_lisa", "char_248_mgllan", "char_1012_skadi2", "char_2023_ling", "char_250_phatom", "char_322_lmlee", "char_400_weedy", "char_225_haak", "char_474_glady", "char_437_mizuki", "char_1023_ghost2", "char_147_shining", "char_179_cgbird", "char_003_kalts", "char_4042_lumen", "char_136_hsguma", "char_202_demkni", "char_423_blemsh", "char_2014_nian", "char_311_mudrok", "char_416_zumama", "char_4039_horn", "char_264_f12yin", "char_172_svrash", "char_293_thorns", "char_010_chen", "char_4009_irene", "char_017_huang", "char_350_surtr", "char_188_helage", "char_485_pallas", "char_1014_nearl2", "char_230_savage", "char_282_catap", "char_283_midn", "char_137_brownb", "char_347_jaksel", "char_164_nightm", "char_220_grani", "char_263_skadi", "char_1001_amiya2"]
OPERATOR_CN_NAMES = ["芬", "香草", "预备干员-近战", "翎羽", "玫兰莎", "泡普卡", "卡缇", "米格鲁", "斑点", "克洛丝", "安德切尔", "预备干员-狙击", "炎熔", "芙蓉", "安赛尔", "预备干员-后勤", "史都华德", "预备干员-术师", "梓兰", "夜烟", "远山", "格雷伊", "卡达", "深靛", "布丁", "杰西卡", "流星", "红云", "梅", "白雪", "松果", "安比尔", "酸糖", "讯使", "清道夫", "红豆", "桃金娘", "豆苗", "杜宾", "缠丸", "断罪者", "霜叶", "艾丝黛尔", "慕斯", "刻刀", "宴", "芳汀", "砾", "孑", "暗索", "末药", "嘉维尔", "苏苏洛", "调香师", "清流", "褐果", "角峰", "蛇屠箱", "泡泡", "古米", "坚雷", "深海色", "地灵", "波登可", "罗比菈塔", "伊桑", "阿消", "白面鸮", "微风", "凛冬", "德克萨斯", "贾维", "苇草", "野鬃", "极境", "夜半", "诗怀雅", "鞭刃", "芙兰卡", "炎客", "Sharp", "因陀罗", "燧石", "拉普兰德", "断崖", "柏喙", "战车", "幽灵鲨", "布洛卡", "星极", "铸铁", "赤冬", "羽毛笔", "龙舌兰", "蓝毒", "白金", "灰喉", "Stormeye", "四月", "寒芒克洛丝", "陨星", "慑砂", "送葬人", "奥斯塔", "阿米娅", "苦艾", "特米米", "天火", "Pith", "惊蛰", "蜜蜡", "莱恩哈特", "薄绿", "爱丽丝", "炎狱炎熔", "蚀清", "耶拉", "洛洛", "梅尔", "稀音", "赫默", "华法琳", "亚叶", "Touch", "锡兰", "絮雨", "图耶", "桑葚", "蜜莓", "濯尘芙蓉", "临光", "吽", "红", "槐琥", "卡夫卡", "乌有", "雷蛇", "可颂", "拜松", "火神", "石棉", "暮落", "暮落", "车尔尼", "闪击", "暴雨", "灰毫", "极光", "普罗旺斯", "守林人", "安哲拉", "熔泉", "埃拉托 ", "崖心", "雪雉", "初雪", "巫恋", "真理", "格劳克斯", "掠风", "空", "海蒂", "月禾", "九色鹿", "夏栎", "狮蝎", "绮良", "食铁兽", "见行者", "罗宾", "霜华", "贝娜", "风丸", "能天使", "空弦", "灰烬", "黑", "远牙", "W", "菲亚梅塔", "早露", "迷迭香", "假日威龙陈", "推进之王", "风笛", "嵯峨", "琴柳", "焰尾", "伊芙利特", "莫斯提马", "艾雅法拉", "刻俄柏", "夕", "异客", "卡涅利安", "澄闪", "黑键", "灵知", "安洁莉娜", "铃兰", "麦哲伦", "浊心斯卡蒂", "令", "傀影", "老鲤", "温蒂", "阿", "歌蕾蒂娅", "水月", "归溟幽灵鲨", "闪灵", "夜莺", "凯尔希", "流明", "星熊", "塞雷娅", "瑕光", "年", "泥岩", "森蚺", "号角", "山", "银灰", "棘刺", "陈", "艾丽妮", "煌", "史尔特尔", "赫拉格", "帕拉斯", "耀骑士临光", "暴行", "空爆", "月见夜", "猎蜂", "杰克", "夜魔", "格拉尼", "斯卡蒂", "阿米娅(近卫)"]

class VikScraper():
  def setup_chrome_driver(self):
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  def teardown_method(self):
    self.driver.quit()

  def initialize_page(self):
    self.driver.get("https://viktorlab.cn/akdata/dps/#")
    self.driver.set_window_size(1542, 1050)
    try:
      WebDriverWait(self.driver, 120).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "div.card.mb-2"))) # wait for first card to load for at least a minute
    except TimeoutException:
      print("Timed out. Restarting Browser.")
      test.teardown_method()
      # self.driver.initialize_page()
    WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "figure > img"))) # character portrait to load

  def scrape_operator(self, op_name, elite_level, op_level, mod_x, mod_level, enemy_def, enemy_mr):
    self.result = {}
    op_name = op_name.strip() # for some reason, Erato's name has a space
    if op_name in ["Lancet-2", "Castle-3", "THRM-EX", "正义骑士号", "夜刀", "黑角", "巡林者", "杜林", "12F"]:
      print("Skipping 2-star operator " + op_name)
      return
    elif op_name in ["预备干员-近战", "预备干员-狙击", "预备干员-后勤", "预备干员-术师"]:
      print("Skipping reserves operator " + op_name)
      return
    elif op_name in ["Sharp", "Pith", "Touch", "Stormeye"]:
      op_name  = "[集成战略]" + op_name

    # fill all forms
    self.driver.find_element(By.CSS_SELECTOR, ".dps__enemy-def").clear()
    self.driver.find_element(By.CSS_SELECTOR, ".dps__enemy-def").send_keys(str(enemy_def))
    self.driver.find_element(By.CSS_SELECTOR, ".dps__enemy-mr").clear()
    self.driver.find_element(By.CSS_SELECTOR, ".dps__enemy-mr").send_keys(str(enemy_mr))
    # click outside fields to update all values
    self.driver.find_element(By.CSS_SELECTOR, ".l-main").click()

    # click first instance of character portrait
    retry = 0
    while retry < 3:
      try:
         self.driver.find_element(By.CSS_SELECTOR, "figure > img").click()
         break
      except NoSuchElementException:
        print("Warning: Something went wrong. Retry: " + retry)
        retry = retry + 1

    # wait for characters to load
    WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.ID, "vue-dialog")))

    # select character by name on page
    self.driver.find_element(By.LINK_TEXT, op_name).click()

    # select elite level
    select_object = Select(self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) .dps__phase"))
    try:
      select_object.select_by_index(elite_level)
    except NoSuchElementException:
      print("Element not found. Assuming default (max) elite level")

    # select level
    select_object = Select(self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) .dps__level"))
    try:
      select_object.select_by_index(op_level-1)
    except NoSuchElementException:
      print("Element not found. Assuming default (max) operator level")

    # check if operator has modules
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) .dps__equip").text
    if (self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) .dps__equip").text == ''):
        print("This operator has no module")
    elif (mod_x == 0):
        print("Skipping module")
    else:
        # select module
        select_object = Select(self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) .dps__equip"))
        select_object.select_by_index(mod_x-1)

        # select module level
        select_object = Select(self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) .dps__equip_level"))
        select_object.select_by_index(mod_level-1)

    for skill_level in range(3):
      # select skill
      select_object = Select(self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) .dps__skill"))
      try:
        select_object.select_by_index(skill_level)
      except NoSuchElementException:
        # Element not found. Assuming skill doesn't exist
        break

      # grab period, skill dps, average dps
      self.result["skill" + str(skill_level+1) + "_period_"] = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .dps__period").text
      self.result["skill" + str(skill_level+1) + "_sk_dps_"] = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .dps__s_dps").text
      self.result["skill" + str(skill_level+1) + "_av_dps_"] = self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(2) > .dps__g_dps").text

    return self.result

test = VikScraper()
print("Preparing Chrome")
test.setup_chrome_driver()
print("Loading Page")
test.initialize_page()
start_time = time()
# for cn_name in OPERATOR_CN_NAMES:
#   print("Scraping: " + cn_name)
#   results = test.scrape_operator(op_name=cn_name, elite_level=2, op_level=70, mod_x=0, mod_level=0, enemy_def=300, enemy_mr=30)
#   print(results)
# print( "Completed after: " + str(timedelta(seconds=time()-start_time)) )
for i in range(len(OPERATOR_CN_NAMES)):
  cn_name = OPERATOR_CN_NAMES[i]
  id = OPERATOR_IDS[i]
  print("Scraping: " + cn_name + " aka " + id)
  results = test.scrape_operator(op_name=cn_name, elite_level=2, op_level=70, mod_x=0, mod_level=0, enemy_def=300, enemy_mr=30)
  print(results)
print( "Completed after: " + str(timedelta(seconds=time()-start_time)) )

import code
code.interact(local=locals())

test.teardown_method()
