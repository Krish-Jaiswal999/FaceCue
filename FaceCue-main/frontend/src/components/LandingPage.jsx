import Nav from "./Nav"
import Hero from "./Hero"
import HowItWorks from "./HowItWorks"
import EmotionSpectrum from "./EmotionSpectrum"
import CoachingPreview from "./CoachingPreview"
import UseCases from "./UseCases"
import FinalCta from "./FinalCta"
import Footer from "./Footer"

export default function LandingPage() {
  return (
    <>
      <Nav />
      <main>
        <Hero />
        <HowItWorks />
        <EmotionSpectrum />
        <CoachingPreview />
        <UseCases />
        <FinalCta />
      </main>
      <Footer />
    </>
  )
}
