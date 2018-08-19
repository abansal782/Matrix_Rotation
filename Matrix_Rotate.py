def rotate(img,rows,columns,flag):
    img3=[]
    if flag==1:
#Moving 90 degree clock-wise
        for i in range(columns):
            d=rows-1
            img2=[]
            for j in range(rows):
                img2.append(img[d][i])
                d=d-1
            img3.append(list(img2))
        return img3
    elif flag==0:
#Moving 90 degree anticlockwise direction
        for i in range(columns):
            d=columns-1-i
#            print(d)
            img2=[]
            for j in range(rows):
                img2.append(img[j][d])
            img3.append(list(img2))
        return img3
    else:
        print("Flag can be either 1 or 0")


lis=[[2,1,3],[8,4,5],[6,9,7]]
new_lis=rotate(lis,len(lis),len(lis[0]),0)
print("After Rotation Matrix Will be = ",new_lis)
