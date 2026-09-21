const USES = [
  "Before a video interview",
  "Warming up for a scene",
  "Rehearsing a hard conversation",
  "Learning to read your own face",
]

export default function UseCases() {
  return (
    <section className="section section-tinted">
      <div className="section-inner">
        <h2 className="section-title">A few minutes, whenever it matters</h2>
        <ul className="usecase-list">
          {USES.map((u) => (
            <li className="usecase-item" key={u}>{u}</li>
          ))}
        </ul>
      </div>
    </section>
  )
}
