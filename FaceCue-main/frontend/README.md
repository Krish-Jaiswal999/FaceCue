# FaceCue frontend

React + Vite frontend for FaceCue. Currently ships the landing page only;
the practice-session screen (the emotion picker, upload, and coaching chat
in `../templates/`) hasn't been ported over yet.

## Develop

    npm install
    npm run dev

## Build

    npm run build

Outputs a static site to `dist/`.

## Wiring up to the backend

The FastAPI app currently serves `../templates` as static files at `/`
(see `app/__init__.py`). Once the rest of the app is ported into this
React project, point that `StaticFiles` mount at `frontend/dist` instead
and run `npm run build` as part of your deploy step.
