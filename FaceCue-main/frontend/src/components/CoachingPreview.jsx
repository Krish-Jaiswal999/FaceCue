export default function CoachingPreview() {
  return (
    <section className="section" id="coaching">
      <div className="section-inner coaching-grid">
        <div className="coaching-quote-wrap">
          <blockquote className="coaching-quote">
            You're getting the eyes right — brows lifted, lids open. But
            surprise lives in the mouth too: let your jaw drop slightly
            instead of stretching your lips wide. Right now that reads
            closer to happy.
          </blockquote>
          <p className="coaching-quote-caption">— from a practice session, target: surprise</p>
        </div>

        <div className="coaching-explainer">
          <h2 className="section-title">Feedback grounded in what your face is actually doing</h2>
          <p>
            A landmark model locates your eyes, nose, and mouth. A
            classifier trained on labeled expressions scores the result
            against all seven categories, not just the one you picked.
          </p>
          <p>
            Then a coach turns those numbers into a sentence you can act
            on — not "try again," but which muscle to move and how far.
          </p>
        </div>
      </div>
    </section>
  )
}
