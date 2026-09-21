import { useEffect, useState } from "react"

const RADIUS = 42
const CIRCUMFERENCE = 2 * Math.PI * RADIUS

export default function AnalysisDial({ value, color, active }) {
  const [display, setDisplay] = useState(0)

  useEffect(() => {
    if (!active) return
    const start = performance.now()
    const duration = 1100
    let frame

    const tick = (now) => {
      const t = Math.min(1, (now - start) / duration)
      const eased = 1 - Math.pow(1 - t, 3)
      setDisplay(Math.round(eased * value))
      if (t < 1) frame = requestAnimationFrame(tick)
    }
    frame = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(frame)
  }, [active, value])

  const offset = CIRCUMFERENCE - (active ? value / 100 : 0) * CIRCUMFERENCE

  return (
    <div className="dial-wrap">
      <svg className="dial-svg" viewBox="0 0 100 100" width="104" height="104">
        <circle className="dial-track" cx="50" cy="50" r={RADIUS} />
        <circle
          className="dial-value"
          cx="50"
          cy="50"
          r={RADIUS}
          style={{
            stroke: color,
            strokeDasharray: CIRCUMFERENCE,
            strokeDashoffset: offset,
          }}
        />
      </svg>
      <div className="dial-center">
        <span className="dial-percent">{display}%</span>
        <span className="dial-caption">match</span>
      </div>
    </div>
  )
}
