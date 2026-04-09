# Documentation for BackEND (ver. 1)

## Authentication & Accounting

All functional require a **JWT Bearer Token** in the header:
`Authorization: Bearer <your_access_token>`

### 1. User Registration
* **URL:** `/api/register/`
* **Method:** `POST`
* **Access:** Public
* **Payload:**
    ```json
    {
        "username": "Tang Tang",
        "password": "endfield_industry_mad_woman",
        "email": "sfmbldfkbnln@mail.chinese",
        "first_name": "Tang",
        "last_name": "Tang"
    }
    ```

### 2. Login (Obtain Token)
* **URL:** `/api/token/`
* **Method:** `POST`
* **Access:** Public
* **Description:** Exchange credentials for a JWT Access and Refresh token.

---

## Kitten Management (CRUD)

**Endpoint:** `/api/kittens/`

| Method | Description | Access |
| :--- | :--- | :--- |
| `GET` | List all available kittens | Authenticated |
| `POST` | Create a new kitten entry | Authenticated |
| `GET` | Retrieve details of a specific kitten (`/api/kittens/{id}/`) | Authenticated |
| `PUT` | Update all fields of a kitten | Owner/Admin |
| `PATCH` | Update specific fields (e.g., just the name) | Owner/Admin |
| `DELETE` | Remove a kitten from the database | Owner/Admin |

**Sample POST/PUT Body:**
```json
{
    "name": "Fenya",
    "breed": "ordinary kot",
    "age_months": 666,
    "description": "Very cool cat",
    "image_url": "тут могла быть ссылка-реклама на изображение",
    "location": 1
}
```
## Messaging System
**Endpoint:** `/api/messages/`
### 1. Send a Message
* **Method:** `POST`
* **Access:** Authenticated
* **Payload:**
    ```json
    {
        "content": "Is this kitten still available for adoption?",
        "tag": "REQ",
        "kitten": 5
    }
    ```
* **Message Tags:** To help with "Accounting" and organization, messages must include one of these tags:
    * `REQ`: Request for adoption.
    * `QUE`: General question.
    * `ADV`: Advice or tips.
    * `NON`: No specific category.

### 2. View Inbox
* **Method:** `GET`
* **Access:** Authenticated
* **Description:** Returns a list of messages where the current user is the sender.

---

## Location & Address System

Before a kitten can be posted, it should be linked to an address. 
**Endpoint:** `/api/addresses/`

### 1. List Locations
* **Method:** `GET`
* **Access:** Authenticated
* **Description:** Useful for search by location.

### 2. Create a Location
* **Method:** `POST`
* **Access:** Authenticated
* **Payload:**
    ```json
    {
        "city": "Almaty",
        "street": "Tole Bi",
        "building_number": "59",
        "apartment_number": "101"
    }
    ```

### 3. Retrieve Single Address
* **URL:** `/api/addresses/{id}/`
* **Method:** `GET`
* **Description:** Fetches the full address details for a specific ID.

---

##  Model Relationships (For Frontend Dev)

When your Angular developer is building the forms, they need to know these ID links:

1.  **Kitten -> Location:** When creating a Kitten, the `location` field must be the **ID** (integer) of an existing Address.
2.  **Message -> Kitten:** When sending a Message, the `kitten` field must be the **ID** of the kitten being discussed.
3.  **Automatic User Links:** The `owner` of a Kitten is automatically set to the user who `POST`ed it.
    * The `sender` of a Message is automatically set to the user who `POST`ed it.