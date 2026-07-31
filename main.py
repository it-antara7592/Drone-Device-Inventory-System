from pymongo import MongoClient
client=MongoClient(host="localhost", port=27017)
db=client["DDInventorySystem_414"]
collection=db["DroneDevices_414"]

def create_dronerecord():
    try:
        droneId=input("Enter the Drone ID:").upper()
        model=input("Enter the Drone Model:")
        manufacturer=input("Enter the Drone Manufacturer Name:")
        serialNumber=input("Enter the Drone serial number:").upper()
        batteryCapacity=input("Enter the Drone Battery Capacity:")
        while True:
            status=input("Enter the Drone Status(Available/ Working /Unavailable):").capitalize()
            if status=='Available':
                break
            elif status=='Working':
                break
            elif status=='Unavailable':
                break
            else:
                print("Entered value is not accepted, Try Again!") 
        purchaseDate=input("Enter the Drone Purchase Date:")
        location=input("Enter the Drone Location:")
        assignedOperator=input("Enter the Assigned Operator of the Drone :")
        maintenanceDate=input("Enter the Drone Maintenance Date:")
        while True:
            conditionStatus=input("Enter the Drone Current Condition(Working/ Repair /Obsolete):").capitalize()
            if conditionStatus=='Working':
                break
            elif conditionStatus=='Repair':
                break
            elif conditionStatus=='Obsolete':
                break
            else:
                print("Entered value is not accepted, Try Again!")
        drone={
                "droneId":droneId,
                "model":model,
                "manufacturer":manufacturer,
                "serialNumber":serialNumber,
                "batteryCapacity":batteryCapacity,
                "status":status,
                "purchaseDate":purchaseDate,
                "location":location,
                "assignedOperator":assignedOperator,
                "maintenanceDate":maintenanceDate,
                "conditionStatus":conditionStatus
                }
        collection.insert_one(drone)
        print("Drone Data Inserted Succesfully")
    except Exception as k:
        print(str(k))

def print_dronedata(dronerec):
    print("\nDrone Data:-")
    for drec in dronerec:
        print(drec)


def search_dronedata():
    try:
        print("\nSearch Drone Data Based On This Criteria")
        print("1. Drone ID")
        print("2. Model Number")
        print("3. Manufacturer")
        print("4. Serial Number")
        print("5. Battery Capacity")
        print("6. Status")
        print("7. Purchase Date")
        print("8. Location")
        print("9. Assigned Operator")
        print("10. Maintenance Date")
        print("11. Condition Status")
        finddata=input("Enter your choice(1-11):")
        if finddata=='1':
            data=input("Enter the Drone ID:").upper()
            dronerec=collection.find({"droneId":data})
            drone_count=collection.count_documents({"droneId":data})
            if drone_count>0:
                print("This Drone Id Exits!")
                print_dronedata(dronerec)
            else:
                print("This Drone Id does not Exists")
                
        elif finddata=='2':
            data=input("Enter the Model Number:")
            dronerec=collection.find({"model":data})
            drone_count=collection.count_documents({"model":data})
            if drone_count>0:
                print("This Model Number Exits!")
                print_dronedata(dronerec)
            else:
                print("This Model Number does not Exists")

        elif finddata=='3':
            data=input("Enter the Manufacturer:")
            dronerec=collection.find({"manufacturer":data})
            drone_count=collection.count_documents({"manufacturer":data})
            if drone_count>0:
                print("This Manufacturer Name Exists!")
                print_dronedata(dronerec)
            else:
                print("This Manufacturer Name does not Exists")

        elif finddata=='4':
            data=input("Enter the Serial Number:").upper()
            dronerec=collection.find({"serialNumber":data})
            drone_count=collection.count_documents({"serialNumber":data})
            if drone_count>0:
                print("This Serial Number Exits!")
                print_dronedata(dronerec)
            else:
                print("This Serial Number does not Exists")
            
        elif finddata=='5':
            data=input("Enter the Battery Capacity:")
            dronerec=collection.find({"batteryCapacity":data})
            drone_count=collection.count_documents({"batteryCapacity":data})
            if drone_count>0:
                print("Battery Capacity Exits!")
                print_dronedata(dronerec)
            else:
                print("Battery Capacity does not Exists")   
                
        elif finddata=='6':
            data=input("Enter the Status:").capitalize()
            dronerec=collection.find({"status":data})
            drone_count=collection.count_documents({"status":data})
            if drone_count>0:
                print("This Status Value Exits!")
                print_dronedata(dronerec)
            else:
                print("This Status Value does not Exists")
            
        elif finddata=='7':
            data=input("Enter the Purchase Date:")
            dronerec=collection.find({"purchaseDate":data})
            drone_count=collection.count_documents({"purchaseDate":data})
            if drone_count>0:
                print("This Purchase Date Exits!")
                print_dronedata(dronerec)
            else:
                print("This Purchase Date does not Exists")
            
        elif finddata=='8':
            data=input("Enter the Location:")
            dronerec=collection.find({"location":data})
            drone_count=collection.count_documents({"location":data})
            if drone_count>0:
                print("This Location of Drone Device Exits!")
                print_dronedata(dronerec)
            else:
                print("This Location of Drone Device was not found")

        elif finddata=='9':
            data=input("Enter the Assigned Operator:")
            dronerec=collection.find({"assignedOperator":data})
            drone_count=collection.count_documents({"assignedOperator":data})
            if drone_count>0:
                print("This Assigned Operator Exits!")
                print_dronedata(dronerec)
            else:
                print("This Assigned Operator does not Exists")

        elif finddata=='10':
            data=input("Enter the Maintenance Date:")
            dronerec=collection.find({"maintenanceDate":data})
            drone_count=collection.count_documents({"maintenanceDate":data})
            if drone_count>0:
                print("This Maintenance Date Exits!")
                print_dronedata(dronerec)
            else:
                print("This Maintenance Date does not Exists")

        elif finddata=='11':
            data=input("Enter the Condition Status:").capitalize()
            dronerec=collection.find({"conditionStatus":data})
            drone_count=collection.count_documents({"conditionStatus":data})
            if drone_count>0:
                print("This Condition Status Exits!")
                print_dronedata(dronerec)
            else:
                print("This Condition Status does not Exists")
        else:
            print("Given Choice Does Not Match Any Field")

    except Exception as k:
        print(str(k))

    

def update_dronedata():
    try:
        droneId=input("Enter the Drone ID: ").upper()
        drone=collection.find_one({"droneId":droneId},{"droneId":1})
        if drone is not None:
            print("\nDrone Data Update List:-")
            print("1. Status")
            print("2. Location")
            print("3. Assigned Operator")
            print("4. Maintenance Date")
            print("5. Condition Status")
            update=input("Enter your choice(1-5):")
            if update=='1':
                while True:
                    data=input("Enter the updated status(Available/ Working /Unavailable): ").capitalize()
                    if data=='Available':
                        break
                    elif data=='Working':
                        break
                    elif data=='Unavailable':
                        break
                    else:
                        print("Entered value is not accepted, Try Again!") 
                collection.update_one({"droneId":droneId},{"$set":{"status":data}})
                print(f"Status of {droneId} Updated Successfully.")
            elif update=='2':
                data=input("Enter the updated location: ")
                collection.update_one({"droneId":droneId},{"$set":{"location":data}})
                print(f"Location of {droneId} Updated Successfully.")
            elif update=='3':
                data=input("Enter the updated Assigned Operator: ")
                collection.update_one({"droneId":droneId},{"$set":{"assignedOperator":data}})
                print(f"Assigned Operator of {droneId} Updated Successfully.")
            elif update=='4':
                data=input("Enter the updated Maintenance Date in(yyyy-mm-dd format): ")
                collection.update_one({"droneId":droneId},{"$set":{"maintenanceDate":data}})
                print(f"Maintenance Data of {droneId} Updated Successfully.")
            elif update=='5':
                while True:
                    data=input("Enter the updated Condition Status(Working/ Repair /Obsolete): ").capitalize()
                    if data=='Working':
                        break
                    elif data=='Repair':
                        break
                    elif data=='Obsolete':
                        break
                    else:
                        print("Entered value is not accepted, Try Again!") 

                collection.update_one({"droneId":droneId},{"$set":{"conditionStatus":data}})
                print(f"Condition Status of {droneId} Updated Successfully.")
            else:
                print("No Data to Update")

        else:
            print("Drone ID not found.")
    except Exception as k:
        print(str(k))


def read_dronerecord():
    try:
        dronerec=collection.find()
        if collection.count_documents({})==0:
            print("No drone records found.")
        else:
            print_dronedata(dronerec)
    except Exception as k:
        print(str(k))

def delete_droneallrecords():
    try:
        collection.delete_many({})
        print("All Drone Data Deleted Successfully")
    except Exception as k:
        print(str(k))

def delete_droneconditionobsolete():
    try:
        choice=input("Do you want to delete the data of all drones whose condition is obsolete: ").lower()
        if choice=='yes':
            collection.delete_many({"conditionStatus":"Obsolete"})
            print("All Drone Data with Obsolete Condition Are Successfully Deleted")

        else:
            print("No Drone Data is Deleted")
    except Exception as k:
        print(str(k))

def display_menu():
    print("\nInventory Operations Menu ")
    print("1. Insert Drone Data")
    print("2. Read All Drone Data")
    print("3. Update a Drone Data")
    print("4. Search a Drone Data")
    print("5. Delete Drone Data having Obsolete Condition")
    print("6. Delete All Drone Data")
    print("7. Exit")

def main():
    while True:
        display_menu()
        choice=input("\nEnter the choice(1-7):")
        if choice=='1':
            create_dronerecord()
        elif choice=='2':
            read_dronerecord()
        elif choice=='3':
            update_dronedata()
        elif choice=='4':
            search_dronedata()
        elif choice=='5':
            delete_droneconditionobsolete()
        elif choice=='6':
            delete_droneallrecords()
        elif choice=='7':
            print("Program Finished")
            break
        else:
            print("Incorrect Choice, Try Again!")


if __name__=="__main__":
    main()
# Driver Code
# #create_dronerecord()
# read_dronerecord()
