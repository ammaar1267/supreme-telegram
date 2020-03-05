n = int(input('Total Income: '))
total_saving = 50
lower_limit = 350
middle_limit = 500
higher_limit = 700

if n < lower_limit:
    print('No Taxable Income')
elif lower_limit <= n < middle_limit:
    print('Your Income is Taxable')
    print('Do you have any Savings y for Yes & n for No:')
    s = input()
    if s == 'y':
        ts = int(input('Please tell me your total savings: '))
        if ts >= 50:
            if n-50 > 350:
                print('Your Taxable incomes Rs: ', n-50)
                print('You should pay Rs:', (n-50-350)*0.1, 'As a tax')
            else:
                print('Due to saving Your income is not taxable')
        else:
            if n-ts <=lower_limit:
                print('Your Taxable income below 350')
                print('No Tax Required to Pay')
            else:
                print('Your Taxable Income is Rs: ', n-ts)
                print('You should pay Rs:', (n-ts-350)*0.1, 'As a tax')


    else:
        print('No saving, So Taxable Income is: ', n)
        print('You should pay Rs:', (n-lower_limit)*0.1, 'As a tax')

elif middle_limit <= n < higher_limit:
    print('Your Income is Taxable')
    print('Do you have any Savings y for Yes & n for No:')
    s = input()
    if s == 'y':
        ts = int(input('Please tell me your total savings: '))
        if ts >= total_saving:
            if n-ts >= middle_limit:
                print('Your Taxable incomes Rs: ', n - total_saving)
                print('You should pay Rs:', ((n-total_saving-middle_limit)*0.2 + 15) , 'As a tax')
        else:
            if n-ts <=lower_limit:
                print('Your Taxable income below 350')
                print('No Tax Required to Pay')
            else:
                print('Your Taxable Income is Rs: ', n-ts)
                print('You should pay Rs:', (n-ts)*0.1, 'As a tax')