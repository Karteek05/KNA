# KNA

# 🚆 Wheelset & Bogie Inspection Backend (FastAPI)

This FastAPI project powers the backend APIs for submitting and retrieving **wheelset measurement** and **bogie inspection/checksheet** forms, used in railway coach maintenance.

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py               # Entry point
│   ├── models.py             # SQLAlchemy models
│   ├── schemas.py            # Pydantic request/response schemas
│   ├── crud.py               # DB operations
│   ├── database.py           # DB config
│   ├── routes/
│       ├── wheelset.py       # Wheelset routes
│       └── bogie.py          # Bogie routes
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 🔧 Requirements

* Python 3.9+
* FastAPI
* SQLAlchemy
* Uvicorn
* SQLite / PostgreSQL

### 🛠️ Setup Instructions

```bash
# 1. Clone the repo
git clone https://github.com/your/repo-name.git
cd repo-name

# 2. Create a virtual environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn app.main:app --reload
```

API will now be live at: `http://localhost:8000`

Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📨 API Endpoints

### 📌 Wheelset Measurement

#### ➕ POST `/forms/wheel-specifications`

Submit a new wheel specification form.

##### ✅ Request Body

```json
{
  "formNumber": "WHEEL-2025-001",
  "submittedBy": "user_id_123",
  "submittedDate": "2025-07-25",
  "fields": {
    "treadDiameterNew": "915mm",
    "lastShopIssueSize": "837mm",
    "condemningDia": "825mm",
    "wheelGauge": "1600",
    "variationSameAxle": "1mm",
    "variationSameBogie": "2mm",
    "variationSameCoach": "3mm",
    "wheelProfile": "Profile A",
    "intermediateWWP": "Yes",
    "bearingSeatDiameter": "125mm",
    "rollerBearingOuterDia": "155mm",
    "rollerBearingBoreDia": "100mm",
    "rollerBearingWidth": "35mm",
    "axleBoxHousingBoreDia": "140mm",
    "wheelDiscWidth": "85mm",
    "remarks": "Check pending"
  }
}
```

##### ✅ Response

```json
{
  "success": true,
  "message": "Wheel specification submitted successfully.",
  "data": {
    "id": 1,
    "form_number": "WHEEL-2025-001",
    "submitted_by": "user_id_123",
    "submitted_date": "2025-07-25",
    "created_at": "...",
    "updated_at": null
  }
}
```

---

#### 📄 GET `/forms/wheel-specifications`

Query by parameters like `formNumber`, `submittedBy`, or `submittedDate`.

---

### 🧾 Bogie Checksheet

#### ➕ POST `/forms/bogie-checksheet`

Submit bogie inspection and checksheet data.

##### ✅ Request Body

```json
{
  "formNumber": "BOGIE-2025-001",
  "inspectionBy": "user_id_456",
  "inspectionDate": "2025-07-03",
  "bogieDetails": {
    "bogieNo": "BG1234",
    "makerYearBuilt": "RDSO/2018",
    "incomingDivAndDate": "NR / 2025-06-25",
    "deficitComponents": "None",
    "dateOfIOH": "2025-07-01"
  },
  "bogieChecksheet": {
    "bogieFrameCondition": "Good",
    "bolster": "Good",
    "bolsterSuspensionBracket": "Cracked",
    "lowerSpringSeat": "Good",
    "axleGuide": "Worn"
  },
  "bmbcChecksheet": {
    "cylinderBody": "WORN OUT",
    "pistonTrunnion": "GOOD",
    "adjustingTube": "DAMAGED",
    "plungerSpring": "GOOD"
  }
}
```

##### ✅ Response

```json
{
  "success": true,
  "message": "Bogie checksheet submitted successfully.",
  "data": {
    "formNumber": "BOGIE-2025-001",
    "inspectionBy": "user_id_456",
    "status": "Saved"
  }
}
```

---

## 📦 Dependencies

Install all with:

```
pip install -r requirements.txt
```

#### `requirements.txt` sample:

```txt
fastapi
uvicorn
sqlalchemy
pydantic
python-multipart
```

---

## 🛠️ Testing with Postman

* Set `Content-Type: application/json`
* Use `/docs` for Swagger testing
* Always POST using valid JSON format
* Check 422 errors for validation issues

---

## 👨‍🔧 Maintainers

* Karteek Ch. (You)
