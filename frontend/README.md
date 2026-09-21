# FaceCue frontend

React + Vite landing page for FaceCue. The existing practice-session screen
remains in `../templates/` and is available from the landing page at
`/practice`.

## Develop

    npm install
    npm run dev

## Build

    npm run build

Outputs a static site to `dist/`.

## Backend bridge

The FastAPI app serves the practice client at `/practice` and exposes the
existing API routes from the same origin. Build this landing page with
`npm run build` when deploying it separately.
