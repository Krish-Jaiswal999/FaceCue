import Brandmark from "./Brandmark"

export default function Footer() {
  return (
    <footer className="footer">
      <div className="section-inner footer-inner">
        <a className="nav-brand" href="#top">
          <Brandmark size={22} id="footer" />
          <span>FaceCue</span>
        </a>
        <p className="footer-note">Practice expressing emotions, on your own time.</p>
      </div>
    </footer>
  )
}
