def main():
    price_in_dollars_for_one_unit_of_ingredient = {}
    t = int(input())
    for i in range(t):
        binder_name = input().upper()
        print(binder_name)
        m, n, budget = map(int, input().split())
        for j in range(m):
            name, dollars = input().split()
            price_in_dollars_for_one_unit_of_ingredient[name] = int(dollars)
        ans = []
        for j in range(n):
            recipe_name = input()
            number_of_units_of_the_ingredient_requirement = int(input())
            sub_budget = 0
            for k in range(number_of_units_of_the_ingredient_requirement):
                requirement, number = input().split()
                sub_budget += price_in_dollars_for_one_unit_of_ingredient[requirement] * int(number)
            if sub_budget <= budget:
                ans.append([recipe_name, sub_budget])
        ans.sort(key=lambda ans: ans[0])
        ans.sort(key=lambda ans: ans[1])
        if len(ans) == 0:
            print("Too expensive!")
        else:
            for j in range(len(ans)):
                print(ans[j][0])
        print()


if __name__ == "__main__":
    main()
