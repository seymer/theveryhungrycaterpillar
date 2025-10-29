import os
import shutil

# 定义分类和对应的文件列表
categories = {
    "Phonics Videos": [
        "Aa_Phonic_video_1.mp4",
        "Bb_Phonic_video_1.mp4",
        "Cc_Phonic_video.mp4",
        "Dd_Phonic_video.mp4",
        "Ee_Phonic_video.mp4",
        "Gg_Phonic_video.mp4",
        "Hh_Phonic_video.mp4",
        "Ii_Phonic_video_1.mp4",
        "Mm_Phonic_video.mp4",
        "Nn_Phonic_video.mp4",
        "Oo_Phonic_video.mp4",
        "Pp_Phonic_video.mp4",
        "Ss_Phonic_video_1.mp4",
        "Tt_Phonic_video_1.mp4",
        "Uu_Phonic_video.mp4"
    ],
    "Art Crafts Episodes": [
        "ArtCrafts_Ep1_Spider.mp4",
        "ArtCrafts_Ep2_Fruit.mp4",
        "ArtCrafts_Ep3_Colour.mp4",
        "ArtCrafts_Ep4_Cloud.mp4",
        "ArtCrafts_Ep5_DaysOfTheWeek.mp4",
        "ArtCrafts_Ep6_Friends.mp4",
        "ArtCrafts_Ep7_FastNSlow.mp4",
        "ArtCrafts_Ep8_LoudAndQuiet.mp4",
        "ArtCrafts_Ep9_UpAndDown.mp4",
        "ArtCrafts_Ep10_Seahorse.mp4",
        "ArtCrafts_Ep11_Firefly.mp4",
        "ArtCrafts_Ep12_Cats.mp4",
        "ArtCrafts_Ep13_Snow.mp4"
    ],
    "Puppet Episodes": [
        "Puppet_Ep1_Spider.mp4",
        "Puppet_Ep2_Caterpillar.mp4",
        "Puppet_Ep3_Crocodile.mp4",
        "Puppet_Ep4_Rabbit.mp4",
        "Puppet_Ep5_Pelican.mp4",
        "Puppet_Ep6_DuckAndDog.mp4",
        "Puppet_Ep7_PigAndBird.mp4",
        "Puppet_Ep8_SealAndGorillaAndBee.mp4",
        "Puppet_Ep9_FrogAndCricket.mp4",
        "Puppet_Ep10_Cats.mp4",
        "Puppet_Ep11_Sheep.mp4",
        "Puppet_Ep12_Seahorse.mp4",
        "Puppet_Ep13_Firefly.mp4"
    ],
    "Storytime Episodes": [
        "Storytime_Ep1_Spider.mp4",
        "Storytime_Ep2_HungryCaterpillar.mp4",
        "Storytime_Ep3_BlueHorse.mp4",
        "Storytime_Ep4_LittleCloud.mp4",
        "Storytime_Ep5_TodayIsMonday.mp4",
        "Storytime_Ep6_Friends.mp4",
        "Storytime_Ep7_Slowly.mp4",
        "Storytime_Ep8_Cricket.mp4",
        "Storytime_Ep9_ClickBeetle.mp4",
        "Storytime_Ep10_Firefly.mp4",
        "Storytime_Ep11_Seahorse.mp4",
        "Storytime_Ep12_Snow.mp4"
    ],
    "Songs": [
        "ABCSong.mp4",
        "AColorPictureSong.mp4",
        "DoubleDoubleDance.mp4",
        "FiveRubberDucks.mp4",
        "LittleRubberDucks.mp4",
        "MessageFromEric.mp4",
        "RoosterOnTheMoon.mp4",
        "ShapesSong.mp4",
        "TenLittlePenguins.mp4"
    ],
    "Section Videos": [
        "section_creative_arts.mp4",
        "section_learn_to_read.mp4",
        "section_math.mp4",
        "section_nature_science.mp4",
        "section_puzzles.mp4"
    ]
}

# 当前目录
current_dir = os.getcwd()

# 遍历每个分类
for folder_name, file_list in categories.items():
    # 创建文件夹（如果不存在）
    folder_path = os.path.join(current_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    print(f"处理分类: {folder_name}")
    
    # 遍历文件列表
    for filename in file_list:
        source_path = os.path.join(current_dir, filename)
        dest_path = os.path.join(folder_path, filename)
        
        if os.path.exists(source_path):
            shutil.move(source_path, dest_path)
            print(f"  已移动: {filename} -> {folder_name}/")
        else:
            print(f"  警告: 文件不存在: {filename}")

print("所有文件整理完成！")
