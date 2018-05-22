def pascals_triangle(num):
    if num==0:
        return []
    prev=[1]
    main=[list(prev)]
    if num==1:
        return main
    for i in range(1,num):
        a=[1]
        j=1
        while j<len(prev):
            sum=prev[j-1]+prev[j]
            a.append(sum)
            j+=1
        a.append(1)
        prev=a
        main.append(list(a))
    print(main)

pascals_triangle(5)

