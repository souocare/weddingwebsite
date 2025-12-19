# Wedding Website & RSVP System — My Personal Wedding

This repository contains the wedding website and RSVP management system built specifically for my wedding.

Although the project was created for a very personal use case, it was designed in a generic and modular way as best as possible, so that anyone can adapt it for their own weddings/events/projects.

---

## Project Goals

The main goal of this project was to build a self-hosted and flexible system to:

- Manage personalized wedding invitations
- Collect RSVPs online, per person
- Send automated and manual emails
- Provide a simple but complete admin interface
- Avoid dependency on expensive or closed third-party wedding platforms

---

## Design Principles & Key Decisions

This project follows several intentional design decisions. Understanding why these choices were made will help anyone who wants to reuse or extend the system.

---

### 1. RSVP per guest, not only per invitation

In this system, **each guest has their own record**, including:
- Attending status (yes / no)
- Email address
- Dietary preferences
- Email history and confirmations

**Why this matters:**
- Supports partial attendance (e.g. one invite is sent to, for example, 4 people (e.g. same household), and  3 out of 4 guests can attend)
- Allows individual communication
- Eliminates ambiguity when counting guests

---

### 2. Invitations as logical groups

The `invitees` table represents **a logical invitation group**, such as:
- a couple
- a family
- a household

Each invitation contains:
- Custom greeting and paragraph
- Maximum allowed guests
- Public invite link
- Ownership (bride/groom side)

Guests (`guests`) always belong to an invitation.

**Why this matters:**
- Keeps personalization at the group level
- Avoids duplicated text
- Keeps the data model clean and understandable



---

### 3. Simple, explicit database structure (SQLite)

The project uses **SQLite** with explicit tables:
- `invitees`
- `guests`
- `logs`

**Why SQLite:**
- Zero setup
- Perfect for small-to-medium projects
- Easy backups (single file)


---

### 4. Email system designed for flexibility

The email system is **provider-agnostic** and supports:
- SMTP (multiple providers supported)
- HTML templates stored on disk
- Subject templates separated from body templates
- Inline images
- Per-guest personalization

**Why this approach:**
- No vendor lock-in
- Easy to swap providers
- Templates can be edited without touching Python code
- Works well for both automated and manual emails


---

### 5. Manual control over automation

This system intentionally avoids “over-automation”.

Examples:
- No automatic reminders without admin action
- No automatic re-sending
- In general, Admin decides when and who to email

**Why:**
- Avoids spamming guests


---

### 6. Admin interface focused on real usage

The admin panel allows:
- Editing invitations
- Editing individual guests
- Adding guests manually
- Sending emails via multiple modes:
  - CSV upload
  - Manual (existing guest)
  - Manual (new email)
  - Database (all guests)
  - Database (only attending guests)

**Why this matters:**
- Covers last-minute changes
- Supports non-technical workflows
- Avoids forcing “one correct way” to manage data



---

## Database Schema
This project uses SQLite (`wedding.db`). The schema is intentionally small and pragmatic: one table for invitation-level customization (`invitees`), one for per-person RSVP state (`guests`), and one for analytics/audit-style logging (`inviteeslog`).

### High-level diagram

```text
invitees (1) ───────────────< (many) guests
   |
   └── personalization + limits + invite-level flags

inviteeslog  (optional analytics / audit trail)
   └── records page visits + actions

```
### invitees
Represents a logical invitation group (family, couple, household).

- One public invite link
- Shared greeting and paragraph
- Maximum number of guests allowed
- Ownership (bride/groom side)
- Flags related to invite lifecycle (sent, nudges, etc.)

### guests
Represents individual people belonging to an invite.

- One row per person
- Individual attending status
- Email, dietary preferences
- Email confirmation history
- Website confirmations and consent flags

This design allows partial attendance and per-guest communication.

### `inviteeslog` (Visits & actions log)

Stores visits and actions for analytics and debugging.

Each row represents a page visit or action (site, email, quick link, admin-triggered events).

Main fields:
- `invitee_id`: related invite (if known)
- `guest_id`: related guest/person (if applicable)
- `idnames`: human-readable invite reference
- `path`, `query`, `referrer`: request context
- `answer`: semantic action (e.g. `rsvp:yes|website`, `quick:no|email`)
- `created_at`: UTC timestamp

Design choice:
- A single log table is used for both invites and guests.
- `guest_id` is optional, allowing flexible logging without schema duplication.

---

## Screenshots

---

## Project Structure

---

## Technologies Used
- Flask
- SQLite
- HTML/CSS/JS
- SMTP

No frontend framework was used on purpose as the project is small and simple.


---
## Setup & Installation

### Requirements
- Python 3.11+ (recommended: 3.12)
- SMTP credentials for email sending (optional if you want email functionality)

### 1) Clone the repo
```bash
git clone <your-repo-url>
cd WeddingProj
```

### 2) Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3) Install dependencies

This project intentionally keeps dependencies minimal and explicit.

Some optional features (third-party email modules) were used with during development but are not required for the core functionality as there are other alternatives.

If you plan to extend the project (e.g. upload images, integrate Mailjet),
additional dependencies may be installed.

```bash
pip install -r requirements.txt
``` 



### 4) Configure environment variables
Create a `.env` file in the project root with the following variables:


### 5) Run the application
```bash
python run.py
```

Then open:
- Public site: http://127.0.0.1:5005/
- Admin: http://127.0.0.1:5005/admin

---

## Authentication & Security

- Basic admin authentication is implemented using Flask-Login.
- Email sending throttled to avoid abuse


---

## Reusing This Project
You are free to reuse and adapt this project for your own wedding or event. Just make sure to:
- Update all personal details and all info used by me
- Review and adjust email templates
- Test thoroughly before going live
- Secure the admin interface properly
- Change default host/port in `run.py` if needed
- Review dependencies and update as necessary
- Changing SMTP provider


This project is not intended as a SaaS or mass-use platform. It is optimized for private events with human oversight.


---

## Disclaimer

This code was built for a real wedding, with real guests and real communication needs.
Some decisions I made prioritize clarity and control over abstraction. So, if you plan to reuse this code, please review it carefully to ensure it fits your needs. Make sure to test all email flows and data management processes before using it in a live setting. 



---

## Final Note

This project represents both a technical challenge and a personal milestone.

If it helps you build something meaningful for your own event, then it has already fulfilled its purpose.







