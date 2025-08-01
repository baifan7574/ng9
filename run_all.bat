@echo off
chcp 65001 >nul

echo Running: 2222.py ...
python 2222.py

echo ------------------------------
echo Running: patch_homepage.py (补丁 homepage 模板结构，包括 canonical、ads、schema ...) ...
python patch_homepage.py

echo ------------------------------
echo Running: generate_index.py (更新首页展示图片区域) ...
python generate_index.py

echo ------------------------------
echo Running: generate_link_list.py (生成全站链接索引页) ...
python generate_link_list.py

echo ------------------------------
echo ✅ 所有任务已完成!
pause
