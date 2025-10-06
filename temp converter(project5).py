temp=float(input("Enter the temperature:"))

unit=input("Enter unit of temperature (C/K/F):")

conv_unit=input("Enter the unit u want it to be converted in(C/K/F):")

if (unit=="C" and conv_unit=="F"):
    F=(temp*1.8)+32
    print("conv from C to F is",F)

elif (unit=="C" and conv_unit=="K"):
    K=temp+27.15
    print("conv from C to K is",K)

elif (unit=="F" and conv_unit=="C"):
    C=(temp-32)*0.55
    print("conv from F to C is",C)

elif (unit=="F" and conv_unit=="K"):
    K=(temp-32)*0.55+273.15
    print("conv from F to K is",K)

elif(unit=="K" and conv_unit=="C"):
    C=temp-273.15
    print("Conv from K to C is",C)

elif(unit=="K" and conv_unit=="F"):
    F=(temp-273.15)*1.8+32
    print("conv from K to F is",F)

else:
    print("invalid inputtt :( sedd")

