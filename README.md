# FaceCue

FaceCue is a FastAPI application with a vanilla JavaScript practice client and
a React landing page.

## Setup

1. Install the Python dependencies:

	```powershell
	python -m pip install -r requirements.txt
	```

2. Copy `.env.example` to `.env` and set `DATABASE_URL`, `JWT_SECRET_KEY`,
	`GROQ_API_KEY`, and `MASTER_PROMPT`.

3. Provide the model files at `ddamfn/weights/rafdb.pth` and
	`face_landmarker.task`.

4. Start the ASGI server:

	```powershell
	uvicorn asgi:app --reload
	```

Database tables are created on application startup. For production, use a
proper migration tool before changing the schema.

The practice client is available at `/practice`. The React landing page can
be developed separately from `frontend/` with `npm install` and `npm run dev`.
# FaceCue