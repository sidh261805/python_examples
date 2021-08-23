#raise TypeError('wrong data type')
#raise ValueError('wrong data type')
#raise ZeroDivisionError('wrong data type')

#for inheritace raise error in base class for not implemented method
#raise NotImplementedError('Need to define method')   => abstract method / pure virtual function

while True:
    try:
        ......
        # break  => not require with else
    except ValueError:
        print ("....") 
    except ZeroDivisionError as er:
        print(err)
    except:
        print ("....") 
    else:
        print ("..run after try..") 
        break
    finally :
        print ("..run with/without error..") 



###############################################################
raise NametooShort("..run after try..")

class NametooShort(ValueError):
    pass