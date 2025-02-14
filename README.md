# KVK Appointment Monitor

This project checks available appointment dates at KVK: Kamer van Koophandel.

## Description
I was surprised by how fully booked the KVK is, as I had always believed that the Dutch government actively encouraged entrepreneurship. As of February 14, 2025, there is a waitlist of about a month at the major KVK offices. This means that if you want to start your own business, you have to wait a full month to officially get started. In fast-moving fields like AI, this could be detrimental.

Fortunately, there are many last-minute cancellations and rescheduled appointments. However, no one wants to constantly check KVK's calendar hoping for an open slot. Luckily, the KVK (accidentally) allows an API endpoint to be used even when you are not logged in. This enables us to monitor when slots open up and let you book your appointment without having to wait a full month.

Please note that this project can only show whether any timeslot is available on a given day, regardless of the specific timeslot. The API endpoint for finding exact timeslots is properly authenticated and thus hard to automate.

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