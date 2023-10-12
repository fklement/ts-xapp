#This is TS xApp version 1.0.0
import logging
import socket
import time
import os
from threading import Thread, Lock
from ricxappframe.xapp_frame import RMRXapp, rmr, Xapp
from rmr_health_check import RMRHealthCheckXapp
from sdl_health_check import sdl_health_check
from alarm_handlers import handle_handover_failure, handle_data_retrieval_failure, handle_cell_congestion
from path.to.SubscriptionHandler import SubscriptionHandler  # Adjust the import path as necessary

# Initialize logging
logging.basicConfig(level=logging.INFO)

print("Wellcome to start TS-xApp, in this stage we are going to run the TS xApp....")
print("We should test O-RAN compoonet")


def main_menu():
    print("\nWelcome to the Traffic Steering xApp!")
    print("xApp Onboarded and deployed successfully.")
    print("xApp registered via E2.\n")
    
    while True:
        print("\nMenu Options:")
        print("1 - Apply Load Balancing")
        print("2 - Cell Outage Compensation")
        print("3 - Slicing-based Steering")
        print("4 - Service-based Steering")
        print("5 - Energy Efficiency")
        print("6 - Undeploy the TS-xApp")
        print("Enter 'exit' to quit the application.\n")
        
        choice = input("Please select an option: ")

        if choice == '1':
            ts_xapp.run_load_balancing = True  # Start load balancing
            print("Load Balancing applied. See the result in the dashboard.")
        elif choice == '2':
            print("Cell Outage Compensation applied. See the result in the dashboard.")
        elif choice == '3':
            print("Slicing-based Steering applied. See the result in the dashboard.")
        elif choice == '4':
            print("Service-based Steering applied. See the result in the dashboard.")
        elif choice == '5':
            print("Energy Efficiency applied. See the result in the dashboard.")
        elif choice == '6':
            print("TS-xApp undeployed successfully.")
            break
        elif choice.lower() == 'exit':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    rmr_health_check = None
    ts_xapp = None
    try:
        # Initialize RMR health check
        rmr_health_check = RMRHealthCheckXapp()
        if not rmr_health_check.rmr_health_check():
            logging.error("RMR health check failed. Exiting.")
            return

        # Perform SDL health check
        if not sdl_health_check():
            logging.error("SDL health check failed. Exiting.")
            return

        # Initialize and run the Traffic Steering xApp
        ts_xapp = TrafficSteering()
        ts_xapp.on_register()
        Thread(target=ts_xapp.run).start()

        # Start the interactive menu
        main_menu()

      except Exception as e:
        logging.error(f"An error occurred: {e}")

    finally:
        if ts_xapp and ts_xapp.server:
            ts_xapp.server.close()

if __name__ == "__main__":
    main()

