def rotate(img,rows,columns,flag):
    img3=[]
    if flag==1:
#Moving 90 degree clock-wise
        for i in range(rows):
            d=rows-1
            img2=[]
            for j in range(columns):
                img2.append(img[d][i])
                d=d-1
            img3.append(list(img2))
        return img3
    elif flag==0:
#Moving 90 degree anticlockwise direction
        for i in range(rows):
            d=rows-1-i
#            print(d)
            img2=[]
            for j in range(columns):
                img2.append(img[j][d])
            img3.append(list(img2))
        return img3
    else:
        print("Flag can be either 1 or 0")


lis=[[2,1,3],[8,4,5],[6,9,7]]
new_lis=rotate(lis,3,3,0)
print("After Rotation Matrix Will be = ",new_lis)
