import argparse
import logging
import random
import time
from typing import Optional

import requests
from enums import AppointmentServiceIDs, LocationIDs
from utils import format_dates, print_suggestion


def fetch_appointment_dates(location: str, service: str) -> Optional[list[str]]:
    """Fetch available appointment dates from the KVK API."""

    try:
        location_id: str = LocationIDs[location].value
    except KeyError:
        print_suggestion(location, [loc.name for loc in LocationIDs], "location")
        return None

    try:
        appointment_service_id: str = AppointmentServiceIDs[service].value
    except KeyError:
        print_suggestion(service, [svc.name for svc in AppointmentServiceIDs], "service")
        return None

    url = f'https://web-api.kvk.nl/appointments/dates/{appointment_service_id}/{location_id}'
    response = requests.get(url=url, headers={'User-Agent': f'Mozilla/5.0 {random.choice(range(100))}'})

    if response.status_code == 400:
        logging.error("Request rejected due to too many requests. Please try again later.")
    elif response.status_code == 200:
        return format_dates(response.json())
    else:
        logging.error(f"Failed to fetch data: {response.status_code} - {response.text}")

    return None


def monitor_appointments(location: str, service: str, interval: int) -> None:
    """Monitor available appointment dates at regular intervals."""

    logging.info(f"Starting monitor for {service} at {location} every {interval} seconds.")

    available_dates: set[str] = set()
    first_check = True
    while True:
        dates = fetch_appointment_dates(location, service)

        if dates and first_check:
            available_dates = set(dates)
            first_check = False
            continue

        if dates:
            newly_available_dates: set[str] = set(dates).difference(available_dates)
            newly_removed_dates: set[str] = available_dates.difference(set(dates))

            if newly_available_dates:
                logging.info(f"Newly available date(s): {format_dates(newly_available_dates)}")
            if newly_removed_dates:
                logging.info(f"Newly removed date(s): {format_dates(newly_removed_dates)}")

            available_dates = set(dates).copy()
        time.sleep(max(0, interval + random.randint(-500, 500) / 100))

def main() -> None:
    """Main function to parse arguments and fetch or monitor appointment dates."""

    parser = argparse.ArgumentParser(description='Check available appointment dates at KVK.')
    parser.add_argument('location', type=str, help='Location ID (e.g., DEN_HAAG, ROTTERDAM)')
    parser.add_argument('service', type=str, help='Appointment Service ID (e.g., EENMANSZAAK, BEDRIJF_OVERNEMEN)')
    parser.add_argument('--monitor', action='store_true', help='Enable monitoring mode')
    parser.add_argument('--interval', type=int, default=60, help='Monitoring interval in seconds')
    
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    dates = fetch_appointment_dates(args.location.upper(), args.service.upper())
    if dates:
        print(dates)

    if args.monitor:
        monitor_appointments(args.location.upper(), args.service.upper(), args.interval)

if __name__ == '__main__':
    main()