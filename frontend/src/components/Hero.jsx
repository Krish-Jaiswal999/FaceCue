import AnalysisDial from "./AnalysisDial"
import useInView from "../hooks/useInView"

export default function Hero() {
  const [cardRef, cardInView] = useInView({ threshold: 0.5 })

  return (
    <section className="hero" id="top">
      <div className="hero-inner">
        <div className="hero-copy">
          <h1 className="hero-title">
            Say it with your face,<br />not just your words.
          </h1>
          <p className="hero-sub">
            Upload a photo, pick the emotion you meant, and FaceCue tells you
            exactly what your expression is reading as instead — before your
            camera turns on for real.
          </p>
          <div className="hero-actions">
            <a className="btn btn-primary" href="#start">Start a practice session</a>
            <a className="btn btn-ghost" href="#how-it-works">See how it works</a>
          </div>
          <p className="hero-footnote">No account needed to try your first photo.</p>
        </div>

        <div className="hero-visual" ref={cardRef}>
          <div className="analysis-card">
            <div className="analysis-header">
              <span className="analysis-eyebrow">Expression analysis</span>
            </div>

            <div className="analysis-body">
              <AnalysisDial value={71} color="var(--surprise)" active={cardInView} />

              <div className="analysis-stats">
                <div className="stat-row">
                  <span className="stat-label">Target emotion</span>
                  <span className="stat-value">
                    <span className="stat-emoji">😲</span>
                    <span>Surprise</span>
                  </span>
                </div>
                <div className="stat-row">
                  <span className="stat-label">Detected expression</span>
                  <span className="stat-value">
                    <span className="stat-emoji">😊</span>
                    <span>Happy</span>
                  </span>
                </div>
                <div className="stat-row">
                  <span className="stat-label">Confidence</span>
                  <span className="stat-value stat-mono">64.2%</span>
                </div>
              </div>
            </div>

            <p className="analysis-note">
              Your eyebrows lifted the way surprise calls for, but the smile
              is pulling the read toward happy. Try dropping your jaw instead
              of stretching your lips.
            </p>
          </div>
        </div>
      </div>
    </section>
  )
}
