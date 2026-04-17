# check_path.py
import os
import sys

print("当前工作目录:", os.getcwd())
print("脚本所在目录:", os.path.dirname(os.path.abspath(__file__)))

# 检查PyCharm报错的路径
problematic_path = r"D:\2026_code\2026_code\Playgame_Project\pythonProject\alien_invasion"
print(f"报错路径是否存在: {os.path.exists(problematic_path)}")

# 建议的正确路径
correct_path = r"D:\2026_code\2026_code\Playgame_Project\alien_invasion"
print(f"建议路径是否存在: {os.path.exists(correct_path)}")

# 列出当前目录文件
print("\n当前目录文件:")
for file in os.listdir('.'):
    print(f"  - {file}")