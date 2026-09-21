const EMOTIONS = [
  { name: "Happy", emoji: "😊", var: "happy" },
  { name: "Sad", emoji: "😢", var: "sad" },
  { name: "Angry", emoji: "😠", var: "angry" },
  { name: "Fear", emoji: "😨", var: "fear" },
  { name: "Surprise", emoji: "😲", var: "surprise" },
  { name: "Disgust", emoji: "🤢", var: "disgust" },
  { name: "Neutral", emoji: "😐", var: "neutral" },
]

export default function EmotionSpectrum() {
  return (
    <section className="section section-tinted" id="expressions">
      <div className="section-inner">
        <h2 className="section-title">Seven expressions, read the same way every time</h2>
        <p className="section-lede">
          FaceCue doesn't guess in general terms. Every photo gets scored
          against the same seven categories, so you can see exactly which
          one is winning and by how much.
        </p>

        <ul className="emotion-strip">
          {EMOTIONS.map((e) => (
            <li
              className="emotion-chip"
              key={e.name}
              style={{
                "--chip-color": `var(--${e.var})`,
                "--chip-soft": `var(--${e.var}-soft)`,
              }}
            >
              <span className="emotion-chip-emoji" aria-hidden="true">{e.emoji}</span>
              <span className="emotion-chip-name">{e.name}</span>
            </li>
          ))}
        </ul>
      </div>
    </section>
  )
}
