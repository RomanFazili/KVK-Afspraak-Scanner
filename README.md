# KVK Appointment Monitor

This project checks available appointment dates at KVK (Kamer van Koophandel). It is possible to make a monitor.

## Description

The script makes a request to the KVK API to check for available appointment dates at a specified location and for a specified service.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the script using `python kvk.py <location> <service>`.

## Files

- `kvk.py`: The main script to make the request to the KVK API.
- `enums.py`: Contains the enum classes for appointment services and location IDs.
- `utils.py`: Contains helper functions used by the main script.

## Example

To check for available appointment times for the "EENMANSZAAK" service at the "ROTTERDAM" location, run the following command:

```bash
python kvk.py ROTTERDAM EENMANSZAAK
```

To monitor available appointment times for the "EENMANSZAAK" service at the "ROTTERDAM" location every 60 seconds, run the following command:

```bash
python kvk.py ROTTERDAM EENMANSZAAK --monitor --interval 60
```

The script will print any changes in available appointment dates.