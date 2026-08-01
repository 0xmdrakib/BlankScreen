const RELEASE_URL = "https://github.com/0xmdrakib/BlankScreen/releases/latest";
const REPO_URL = "https://github.com/0xmdrakib/BlankScreen";

const features = [
  {
    number: "01",
    title: "Your work keeps moving",
    body: "Downloads, renders, scripts, backups, and long-running tasks continue exactly where you left them.",
  },
  {
    number: "02",
    title: "A calmer OLED canvas",
    body: "Replace bright, static interfaces with a pure-black surface while you wait for the computer to finish.",
  },
  {
    number: "03",
    title: "No cable gymnastics",
    body: "Leave the monitor connected. One tiny utility covers every display without changing your workspace.",
  },
  {
    number: "04",
    title: "Back in one touch",
    body: "Click, press Esc, or use any key. BlankScreen disappears instantly and your desktop is right where it was.",
  },
];

const steps = [
  ["Download", "Grab the latest standalone Windows executable from GitHub Releases."],
  ["Run", "Open BlankScreen.exe. Every connected display turns pure black."],
  ["Return", "Click anywhere or press any key when you want your screen back."],
];

function Arrow() {
  return <span aria-hidden="true">↗</span>;
}

export default function Home() {
  return (
    <main id="main-content">
      <a className="skip-link" href="#main-content">
        Skip to content
      </a>

      <header className="topbar">
        <a className="brand" href="#top" aria-label="BlankScreen home">
          <span className="logo-tile" aria-hidden="true">
            {/* The logo is a local static asset; bypassing image optimization avoids runtime work. */}
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src="/logo.png" alt="" width="34" height="34" />
          </span>
          <span>BlankScreen</span>
        </a>
        <nav aria-label="Primary navigation">
          <a href="#why">Why</a>
          <a href="#how">How it works</a>
          <a href={REPO_URL} target="_blank" rel="noreferrer">
            GitHub
          </a>
          <a className="nav-download" href={RELEASE_URL} target="_blank" rel="noreferrer">
            <span className="nav-desktop">Download</span><span className="nav-mobile">Get</span> <Arrow />
          </a>
        </nav>
      </header>

      <section className="hero" id="top">
        <div className="hero-copy">
          <p className="hero-kicker">A tiny Windows utility</p>
          <h1 className="desktop-headline">
            Keep the work running.
            <span>Let the screen go black.</span>
          </h1>
          <h1 className="mobile-headline">
            Keep working.
            <span>Go black.</span>
          </h1>
          <p className="hero-lede desktop-lede">
            BlankScreen covers every display with pure black while everything behind it keeps working.
            One file. No install. One touch to return.
          </p>
          <p className="hero-lede mobile-lede">
            Downloads, renders, and scripts keep running under a pure-black screen. Tap once to return.
          </p>
          <div className="hero-actions">
            <a className="button button-primary" href={RELEASE_URL} target="_blank" rel="noreferrer">
              Download for Windows <Arrow />
            </a>
            <a className="button button-secondary" href={REPO_URL} target="_blank" rel="noreferrer">
              View source <Arrow />
            </a>
          </div>
          <p className="hero-meta">Windows 10/11 · Standalone EXE · MIT licensed</p>
        </div>

        <div className="product-visual" aria-label="BlankScreen product visual">
          <div className="visual-grid" aria-hidden="true">
            <span /><span /><span /><span /><span /><span />
          </div>
          <div className="visual-heading">
            <span>DISPLAY CONTROL / 01</span>
            <span className="visual-status"><i /> SYSTEM ACTIVE</span>
          </div>
          <div className="visual-core">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img className="hero-logo" src="/logo.png" alt="" width="512" height="512" />
            <div className="black-screen">
              <span>PURE BLACK</span>
              <strong>00</strong>
            </div>
          </div>
          <div className="visual-footer">
            <div><span>Foreground</span><strong>Covered</strong></div>
            <div><span>Background work</span><strong>Running</strong></div>
            <div><span>Return</span><strong>Any key</strong></div>
          </div>
        </div>
      </section>

      <section className="facts" aria-label="Product facts">
        <div><span>01</span><strong>No installer</strong></div>
        <div><span>02</span><strong>Multi-display</strong></div>
        <div><span>03</span><strong>Zero setup</strong></div>
        <div><span>04</span><strong>Open source</strong></div>
      </section>

      <section className="section" id="why">
        <div className="section-heading">
          <p className="eyebrow">Why BlankScreen</p>
          <h2>Your monitor doesn’t need to watch your computer work.</h2>
          <p>
            Long jobs should not mean bright pixels, exposed windows, or reaching behind a desk to pull a cable.
          </p>
        </div>
        <div className="feature-grid">
          {features.map((feature) => (
            <article className="feature-card" key={feature.number}>
              <span>{feature.number}</span>
              <h3>{feature.title}</h3>
              <p>{feature.body}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="section how" id="how">
        <div className="section-heading compact">
          <p className="eyebrow">Three quiet steps</p>
          <h2>Nothing to configure.</h2>
        </div>
        <ol className="step-list">
          {steps.map(([title, body], index) => (
            <li key={title}>
              <span>{String(index + 1).padStart(2, "0")}</span>
              <h3>{title}</h3>
              <p>{body}</p>
            </li>
          ))}
        </ol>
      </section>

      <section className="truth">
        <div>
          <p className="eyebrow">The honest detail</p>
          <h2>Black screen, not powered-off hardware.</h2>
        </div>
        <div className="truth-copy">
          <p>
            BlankScreen draws an opaque black layer over Windows; it does not put your monitor to sleep or stop
            the video signal. That is exactly why your background work stays uninterrupted.
          </p>
          <p>
            Pure black avoids leaving a bright, static interface on an OLED display. LCD backlights remain on,
            so use Windows display sleep when hardware-level power saving is the goal.
          </p>
        </div>
      </section>

      <section className="cta" id="download">
        <div>
          <p className="eyebrow">Tiny tool. Immediate relief.</p>
          <h2>Ready when your screen isn’t.</h2>
        </div>
        <a className="button button-inverse" href={RELEASE_URL} target="_blank" rel="noreferrer">
          Get BlankScreen <Arrow />
        </a>
      </section>

      <footer>
        <div className="footer-brand">
          <span className="logo-tile footer-logo" aria-hidden="true">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src="/logo.png" alt="" width="30" height="30" />
          </span>
          <strong>BlankScreen</strong>
        </div>
        <p>A fun, impactful, minimal mini tool for Windows.</p>
        <div className="footer-links">
          <a href={REPO_URL} target="_blank" rel="noreferrer">GitHub</a>
          <a href={RELEASE_URL} target="_blank" rel="noreferrer">Releases</a>
          <a href={`${REPO_URL}/blob/main/LICENSE`} target="_blank" rel="noreferrer">MIT License</a>
        </div>
        <small>© 2026 Md. Rakib • made with love and passion.</small>
      </footer>
    </main>
  );
}
