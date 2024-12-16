class TrainReservationSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.reserved_seats = {}
        self.waiting_list = []
        self.stations = ["coimbatore", "tiruppur", "erode", "madurai", "palani", "jungstion"]  # Define stations

    def is_valid_station(self, boarding_station, destination_station):
        if boarding_station not in self.stations or destination_station not in self.stations:
            print("Invalid stations provided.")
            return False
        if self.stations.index(boarding_station) >= self.stations.index(destination_station):
            print("Destination station should be after the boarding station.")
            return False
        return True

    def reserve_seat(self, passenger_name, seat_number, boarding_station, destination_station):
        if not self.is_valid_station(boarding_station, destination_station):
            return

        if seat_number in self.reserved_seats:
            print(f"Seat {seat_number} is already reserved.")
            return

        if len(self.reserved_seats) >= self.total_seats:
            self.waiting_list.append((passenger_name, boarding_station, destination_station))
            print(f"All seats are booked. {passenger_name} is added to the waiting list.")
            return

        self.reserved_seats[seat_number] = (passenger_name, boarding_station, destination_station)
        print(f"Seat {seat_number} reserved for {passenger_name} from {boarding_station} to {destination_station}.")

    def cancel_reservation(self, seat_number):
        if seat_number not in self.reserved_seats:
            print(f"No reservation found for seat {seat_number}.")
            return

        passenger_name, boarding_station, destination_station = self.reserved_seats.pop(seat_number)
        print(f"Reservation for seat {seat_number} canceled for {passenger_name}.")

        # Assign the seat to the next waiting passenger if available
        if self.waiting_list:
            next_passenger, next_boarding, next_destination = self.waiting_list.pop(0)
            self.reserved_seats[seat_number] = (next_passenger, next_boarding, next_destination)
            print( f"Seat {seat_number} assigned to {next_passenger} from {next_boarding} to {next_destination} from the waiting list.")

    def print_pnr_details(self):
        print("\nPNR Details:")
        for seat, (passenger, boarding, destination) in sorted(self.reserved_seats.items()):
            print(f"Seat {seat}: {passenger} ({boarding} to {destination})")

        if self.waiting_list:
            print("\nWaiting List:")
            for i, (passenger, boarding, destination) in enumerate(self.waiting_list, start=1):
                print(f"{i}. {passenger} ({boarding} to {destination})")


def main():
    total_seats = 5
    train_system = TrainReservationSystem(total_seats)

    while True:
        print("\nTrain Reservation System")
        print("1. Reserve Seat")
        print("2. Cancel Reservation")
        print("3. Print PNR Details")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            passenger_name = input("Enter passenger name: ").strip()
            seat_number = int(input("Enter seat number (1 to 5): ").strip())
            boarding_station = input("Enter boarding station (coimbatore, tiruppur, erode, madurai, palani, jungstion): ").strip()
            destination_station = input("Enter destination station (coimbatore, tiruppur, erode, madurai, palani, jungstion): ").strip()

            train_system.reserve_seat(passenger_name, seat_number, boarding_station, destination_station)

        elif choice == '2':
            seat_number = int(input("Enter seat number to cancel (1 to 5): ").strip())
            train_system.cancel_reservation(seat_number)

        elif choice == '3':
            train_system.print_pnr_details()

        elif choice == '4':
            print("Thank You Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
