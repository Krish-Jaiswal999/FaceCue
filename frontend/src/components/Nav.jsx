import Brandmark from "./Brandmark"

export default function Nav() {
  return (
    <header className="nav">
      <div className="nav-inner">
        <a className="nav-brand" href="#top">
          <Brandmark size={28} id="nav" />
          <span>FaceCue</span>
        </a>

        <nav className="nav-links" aria-label="Page sections">
          <a href="#how-it-works">How it works</a>
          <a href="#expressions">The expressions</a>
          <a href="#coaching">The coaching</a>
        </nav>

        <div className="nav-actions">
          <a className="nav-signin" href="/practice">Open practice</a>
          <a className="btn btn-primary btn-sm" href="/practice">Start practicing</a>
        </div>
      </div>
    </header>
  )
}
