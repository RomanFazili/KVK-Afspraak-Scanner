# KVK Appointment Monitor

This project checks available appointment dates at KVK: Kamer van Koophandel.

## Description

I was surprised by how fully booked the KVK is. I had always been under the impression that the Dutch government was actively encouraging entrepreneurship. As of writing this on the 14th of February 2025, there is a waitlist of about a month at the major KVK offices.
Fortunately, there are lots of last-minute cancellations and moved appointments. However, no one wants to keep looking at KVK's calendar hoping some spot opens up. Luckily, the KVK (accidentally) allows an API endpoint to be used even when you are not logged in. So we can monitor when slots open up and let you book your appointment without having to wait a full month.
PS: This project is only able to show whether any timeslot is available on a day, regardless of which timeslot that is. The API endpoint for finding exact timeslots is properly authenticated, and thus hard to automate.

## Usage

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the script using `python kvk.py <location> <service>`.

## Files

- `kvk.py`: The main script to make the request to the KVK API.
- `enums.py`: Contains the enum classes for appointment services and location IDs.
- `utils.py`: Contains helper functions used by the main script.

## Example

To check for available appointment dates for the "EENMANSZAAK" service at the "ROTTERDAM" location, run the following command:

```bash
python kvk.py ROTTERDAM EENMANSZAAK
```

To monitor available appointment dates for the "EENMANSZAAK" service at the "ROTTERDAM" location every 60 seconds, run the following command:

```bash
python kvk.py ROTTERDAM EENMANSZAAK --monitor --interval 60
```

The script will log any changes in available appointment dates.