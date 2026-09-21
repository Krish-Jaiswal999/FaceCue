const STEPS = [
  {
    n: "1",
    title: "Pick a target",
    body: "Choose the emotion you're aiming for — happy, sad, angry, afraid, surprised, disgusted, or neutral.",
  },
  {
    n: "2",
    title: "Show your face",
    body: "Upload a photo or take one on the spot. FaceCue finds your face and reads it against seven expression categories.",
  },
  {
    n: "3",
    title: "Read the gap",
    body: "See what registered instead of what you meant, how confident the model is, and one concrete thing to adjust.",
  },
]

export default function HowItWorks() {
  return (
    <section className="section" id="how-it-works">
      <div className="section-inner">
        <h2 className="section-title">Three steps, one photo at a time</h2>

        <ol className="steps">
          {STEPS.map((step) => (
            <li className="step" key={step.n}>
              <span className="step-num">{step.n}</span>
              <h3 className="step-title">{step.title}</h3>
              <p className="step-body">{step.body}</p>
            </li>
          ))}
        </ol>
      </div>
    </section>
  )
}
