status_options_application = {  # These statuses can apply to applications before permit issuance.
    "Application Abandoned": "The permit the application requested was not issued in time. A new application based on updated codes must be submitted. Delays caused by County staff will not be counted against the application time limit.", 
    
    "Application Approved": "The reviews have been approved but the permit has not been issued",
    
    "Application Pending": "The application has not been deemed a complete submittal", 
    
    "Application Under Review": "The application is complete but reviews have not been approved", 
    
    "Application Withdrawn": "The applicant has requested review to be halted and requested a refund of any unused fees.",
    
    "Void": "The record was a test or mistake.",
}

status_options_permit = {  # These statuses can apply to permits after they have been issued.
    "Permit Cancelled": "The permit holder has requested cancellation of the permit and requested a refund of any unused fees.",
    
    "Permit Expired": "Construction was not completed in time. A new permit  application based on updated codes must be submitted. Any work completed before expiration is 'Existing' as defined in the California Existing Building Code.",
    
    "Permit Finaled": "A certificate of occupancy has been issued and/or final inspection approved.",
    
    "Permit Issued": "The permit has been issued but occupancy has not been approved",
    
    "Permit Suspended": "The Building Official has determined that the permit is no longer approved. The permit is suspended until the permit can approved. If a suspended permit  expires, a new permit application based on current codes must be submitted.",
    
    "Void": "The record was a test or mistake.",    
}

status_options_review = {  # These statuses can apply to plan reviews.
    "Approved": "Based on the submitted application and construction documents, the permit is approved by [Division] to be issued. ", 
    
    "Comments Sent": "The application and construction documents cannot be approved as submitted. Comments have been added to the public permit records and will be sent to the applicant once all comments are received.",
    
    "Not Applicable": "The application does not include work that is regulated by this type of review.", 
    
    "Main Review": "The main detailed review is in progress.",
    
    "Pending": "The permit application is incomplete and plan review has not started.", 
    
    "Reviewing Response": "The applicant has submitted updates to the application and/or construction documents in response to the reviewers comments.",
    
    "Void": "The record was a test or mistake.",
}

status_options_inspection = {  # These statuses can apply to inspections,
    "Approved": "The inspection has been approved.",
    
    "Not Applicable": "Based on the scope of work, this inspection is not required.",
    
    "Not Approved": "The inspection was not approved.",
    
    "Not Issued": "The permit status is not 'Permit Issued' so inspections cannot be requested.",
    
    "Not Ready": "The inspector was not able to perform the inspection because the work was not complete or because access to the work was not adequate.",
    
    "Partial Approved": "The partial inspection was approved.",
    
    "Partial Requested": "The permit holder has requested a partial inspection on a large project.",
    
    "Pending": "The permit has been issued, but this inspection has not been requested by the permit holder.",
    
    "Punch List": "Construction was allowed to proceed, but the inspector gave the permit holder a list of items that will need to be reinspected at the next inspection.",
    
    "Red Tag": "A serious code violation was found. All construction activity must cease except for the specific actions requested by the inspector.",
    
    "Requested": "The permit holder has requested this inspection.",
    
    "Scheduled": "The inspector has scheduled the requested inspection.",
    
    "Void": "The record was a test or mistake.",
}

status_options_investigation = {
    "Confirmed Violation": "At least one code violation was identified.",
    
    "No Violation": "The reported violation was not able to be confirmed.",
    
    "Red Tag": "A serious code violation was found. All construction activity must cease except for the specific actions requested by the inspector",
    
    "Void": "The record was a test or mistake.",
}
