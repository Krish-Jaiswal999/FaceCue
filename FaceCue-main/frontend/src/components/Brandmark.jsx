const GRAD_ID_PREFIX = "waveGrad"

export default function Brandmark({ size = 40, id = "default" }) {
  const gradId = `${GRAD_ID_PREFIX}-${id}`
  return (
    <svg
      viewBox="0 0 40 24"
      width={size}
      height={size * 0.6}
      fill="none"
      aria-hidden="true"
    >
      <path
        d="M2 12 Q 7 3, 12 12 T 22 12 T 32 12 T 38 12"
        stroke={`url(#${gradId})`}
        strokeWidth="3"
        strokeLinecap="round"
        fill="none"
      />
      <defs>
        <linearGradient id={gradId} x1="0" y1="0" x2="40" y2="0">
          <stop offset="0" stopColor="#5D3FD3" />
          <stop offset="1" stopColor="#2FB8A6" />
        </linearGradient>
      </defs>
    </svg>
  )
}
