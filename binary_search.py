#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
二分查找法程序
实现递归和迭代两种方式的二分查找算法
"""

def binary_search_recursive(arr, target, left, right):
    """
    递归方式实现二分查找
    
    参数:
        arr: 已排序的数组
        target: 要查找的目标值
        left: 左边界索引
        right: 右边界索引
    
    返回:
        如果找到目标值，返回其索引；否则返回-1
    """
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


def binary_search_iterative(arr, target):
    """
    迭代方式实现二分查找
    
    参数:
        arr: 已排序的数组
        target: 要查找的目标值
    
    返回:
        如果找到目标值，返回其索引；否则返回-1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


def main():
    """主函数，演示二分查找的使用"""
    print("二分查找法程序")
    print("=" * 30)
    
    # 测试数据（已排序的数组）
    test_array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(f"测试数组: {test_array}")
    
    # 测试查找存在的值
    target1 = 10
    print(f"\n查找目标值: {target1}")
    
    # 使用递归方法
    result1_recursive = binary_search_recursive(test_array, target1, 0, len(test_array) - 1)
    print(f"递归方法结果: 索引 {result1_recursive}")
    
    # 使用迭代方法
    result1_iterative = binary_search_iterative(test_array, target1)
    print(f"迭代方法结果: 索引 {result1_iterative}")
    
    # 测试查找不存在的值
    target2 = 15
    print(f"\n查找目标值: {target2}")
    
    # 使用递归方法
    result2_recursive = binary_search_recursive(test_array, target2, 0, len(test_array) - 1)
    print(f"递归方法结果: {'未找到' if result2_recursive == -1 else f'索引 {result2_recursive}'}")
    
    # 使用迭代方法
    result2_iterative = binary_search_iterative(test_array, target2)
    print(f"迭代方法结果: {'未找到' if result2_iterative == -1 else f'索引 {result2_iterative}'}")
    
    # 用户交互测试
    print("\n" + "=" * 30)
    print("交互式测试:")
    
    while True:
        try:
            user_input = input("请输入要查找的数字 (输入 'q' 退出): ").strip()
            
            if user_input.lower() == 'q':
                print("程序结束")
                break
            
            target = int(user_input)
            result = binary_search_iterative(test_array, target)
            
            if result != -1:
                print(f"找到目标值 {target}，位于索引 {result}")
            else:
                print(f"未找到目标值 {target}")
                
        except ValueError:
            print("请输入有效的数字")
        except KeyboardInterrupt:
            print("\n程序被中断")
            break


if __name__ == "__main__":
    main()
