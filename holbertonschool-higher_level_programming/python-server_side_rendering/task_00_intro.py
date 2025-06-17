def generate_invitations(template, attendees):
    # Helper function to log errors or messages
    def log(message):
        print(message)

    # Check input types
    if not isinstance(template, str):
        log(f"Error: Invalid input type for template. Expected str, got {type(template).__name__}.")
        return
    if not isinstance(attendees, list):
        log(f"Error: Invalid input type for attendees. Expected list, got {type(attendees).__name__}.")
        return
    # Check all items in attendees list are dicts
    if not all(isinstance(item, dict) for item in attendees):
        log("Error: Attendees list must contain only dictionaries.")
        return

    # Check empty template
    if template.strip() == "":
        log("Template is empty, no output files generated.")
        return

    # Check empty attendees list
    if len(attendees) == 0:
        log("No data provided, no output files generated.")
        return

    # List of expected placeholders
    placeholders = ["name", "event_title", "event_date", "event_location"]

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        invitation = template
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            # Replace None or missing with "N/A"
            if value is None:
                value = "N/A"
            # Replace the placeholder in the template
            invitation = invitation.replace("{" + placeholder + "}", str(value))
        
        # Write to file output_X.txt
        try:
            filename = f"output_{idx}.txt"
            with open(filename, 'w') as f:
                f.write(invitation)
        except Exception as e:
            log(f"Error writing file {filename}: {e}")
