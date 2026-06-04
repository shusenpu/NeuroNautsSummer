const deck = document.querySelector("#deck");
const shell = document.querySelector(".app-shell");
const frames = Array.from(document.querySelectorAll(".frame"));
const nextBtn = document.querySelector("#nextBtn");
const prevBtn = document.querySelector("#prevBtn");
const notesBtn = document.querySelector("#notesBtn");
const closeNotes = document.querySelector("#closeNotes");
const fullBtn = document.querySelector("#fullBtn");
const notesPanel = document.querySelector("#notesPanel");
const notesText = document.querySelector("#notesText");
const counter = document.querySelector("#counter");
const progressFill = document.querySelector("#progressFill");

let frameIndex = 0;
let fragmentIndex = 0;
let controlsTimer = 0;
const state = {
  attention: 72,
};

function activeFrame() {
  return frames[frameIndex];
}

function fragmentsFor(frame) {
  return Array.from(frame.querySelectorAll("[data-fragment]"));
}

function updateFragments() {
  fragmentsFor(activeFrame()).forEach((fragment, index) => {
    fragment.classList.toggle("is-shown", index < fragmentIndex);
  });
}

function updateProgress() {
  counter.textContent = `${frameIndex + 1} / ${frames.length}`;
  progressFill.style.width = `${((frameIndex + 1) / frames.length) * 100}%`;
  notesText.textContent = activeFrame().dataset.notes || "";
}

function syncVideos() {
  frames.forEach((frame, index) => {
    frame.querySelectorAll("video").forEach((video) => {
      video.muted = true;
      video.loop = true;
      video.playsInline = true;
      video.controls = false;
      if (index === frameIndex) {
        video.play().catch(() => {});
      } else {
        video.pause();
        video.currentTime = 0;
      }
    });
  });
}

function setFrame(nextIndex, nextFragmentIndex = 0) {
  frameIndex = Math.max(0, Math.min(frames.length - 1, nextIndex));
  fragmentIndex = Math.max(0, Math.min(fragmentsFor(frames[frameIndex]).length, nextFragmentIndex));
  frames.forEach((frame, index) => frame.classList.toggle("is-active", index === frameIndex));
  updateFragments();
  updateProgress();
  syncVideos();
}

function next() {
  const fragmentCount = fragmentsFor(activeFrame()).length;
  if (fragmentIndex < fragmentCount) {
    fragmentIndex += 1;
    updateFragments();
    return;
  }
  if (frameIndex < frames.length - 1) setFrame(frameIndex + 1, 0);
}

function prev() {
  if (fragmentIndex > 0) {
    fragmentIndex -= 1;
    updateFragments();
    return;
  }
  if (frameIndex > 0) {
    const previousFrame = frames[frameIndex - 1];
    setFrame(frameIndex - 1, fragmentsFor(previousFrame).length);
  }
}

function toggleNotes(force) {
  const open = typeof force === "boolean" ? force : !notesPanel.classList.contains("is-open");
  notesPanel.classList.toggle("is-open", open);
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen?.();
  } else {
    document.exitFullscreen?.();
  }
}

function showControls() {
  shell.classList.add("controls-visible");
  window.clearTimeout(controlsTimer);
  controlsTimer = window.setTimeout(() => shell.classList.remove("controls-visible"), 1600);
}

function resizeCanvas(canvas) {
  const rect = canvas.getBoundingClientRect();
  const dpr = window.devicePixelRatio || 1;
  const width = Math.max(1, Math.floor(rect.width * dpr));
  const height = Math.max(1, Math.floor(rect.height * dpr));
  if (canvas.width !== width || canvas.height !== height) {
    canvas.width = width;
    canvas.height = height;
  }
  const ctx = canvas.getContext("2d");
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  return { ctx, width: rect.width, height: rect.height };
}

function clear(ctx, width, height, color = "#ffffff") {
  ctx.fillStyle = color;
  ctx.fillRect(0, 0, width, height);
}

function drawText(ctx, text, x, y, size = 18, color = "#102033", weight = 800) {
  ctx.font = `${weight} ${size}px Aptos, system-ui, sans-serif`;
  ctx.fillStyle = color;
  ctx.fillText(text, x, y);
}

function drawCenteredText(ctx, text, x, y, size = 18, color = "#102033", weight = 800) {
  ctx.font = `${weight} ${size}px Aptos, system-ui, sans-serif`;
  ctx.fillStyle = color;
  ctx.textAlign = "center";
  ctx.fillText(text, x, y);
  ctx.textAlign = "left";
}

function roundedRect(ctx, x, y, w, h, r, color) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.lineTo(x + w - r, y);
  ctx.quadraticCurveTo(x + w, y, x + w, y + r);
  ctx.lineTo(x + w, y + h - r);
  ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
  ctx.lineTo(x + r, y + h);
  ctx.quadraticCurveTo(x, y + h, x, y + h - r);
  ctx.lineTo(x, y + r);
  ctx.quadraticCurveTo(x, y, x + r, y);
  ctx.fillStyle = color;
  ctx.fill();
}

function drawArrow(ctx, x1, y1, x2, y2, color = "#009cde", width = 4) {
  const angle = Math.atan2(y2 - y1, x2 - x1);
  ctx.strokeStyle = color;
  ctx.lineWidth = width;
  ctx.lineCap = "round";
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(x2, y2);
  ctx.lineTo(x2 - 14 * Math.cos(angle - Math.PI / 6), y2 - 14 * Math.sin(angle - Math.PI / 6));
  ctx.lineTo(x2 - 14 * Math.cos(angle + Math.PI / 6), y2 - 14 * Math.sin(angle + Math.PI / 6));
  ctx.closePath();
  ctx.fillStyle = color;
  ctx.fill();
}

function movingDot(ctx, points, t, color) {
  const segment = Math.floor(t * points.length) % points.length;
  const nextSegment = (segment + 1) % points.length;
  const local = (t * points.length) % 1;
  const a = points[segment];
  const b = points[nextSegment];
  const x = a.x + (b.x - a.x) * local;
  const y = a.y + (b.y - a.y) * local;
  ctx.beginPath();
  ctx.arc(x, y, 8, 0, Math.PI * 2);
  ctx.fillStyle = color;
  ctx.shadowColor = color;
  ctx.shadowBlur = 18;
  ctx.fill();
  ctx.shadowBlur = 0;
}

function heroSignals(canvas, now) {
  const { ctx, width, height } = resizeCanvas(canvas);
  ctx.clearRect(0, 0, width, height);
  ctx.globalAlpha = 0.75;
  const t = now / 1200;
  for (let i = 0; i < 5; i += 1) {
    const y = height * (0.27 + i * 0.13) + Math.sin(t + i) * 18;
    const start = width * 0.38;
    const end = width * 0.94;
    ctx.strokeStyle = i % 2 ? "#97c800" : "#8dc8e8";
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(start, y);
    for (let x = start; x <= end; x += 24) {
      ctx.lineTo(x, y + Math.sin(x / 62 + t + i) * 18);
    }
    ctx.stroke();
    const dotX = start + ((t * 80 + i * 120) % (end - start));
    ctx.beginPath();
    ctx.arc(dotX, y + Math.sin(dotX / 62 + t + i) * 18, 5, 0, Math.PI * 2);
    ctx.fillStyle = "#ffb81c";
    ctx.fill();
  }
  ctx.globalAlpha = 1;
}

function morningReplay(canvas, now) {
  const { ctx, width, height } = resizeCanvas(canvas);
  clear(ctx, width, height, "#ffffff");
  const t = now / 1000;
  const cx = width / 2;
  const cy = height / 2;
  const scale = Math.max(0.68, Math.min(1.1, Math.min(width / 820, height / 430)));
  const brainR = 70 * scale;
  const cardW = 136 * scale;
  const cardH = 52 * scale;
  const radiusX = Math.min(width * 0.24, brainR + cardW / 2 + 64 * scale);
  const radiusY = Math.min(height * 0.34, brainR + cardH / 2 + 48 * scale);
  const cards = [
    { label: "Wake up", color: "#009cde", angle: -Math.PI / 2, from: "bottom", to: "top" },
    { label: "Find seat", color: "#007a33", angle: 0, from: "left", to: "right" },
    { label: "Recognize", color: "#ffb81c", angle: Math.PI / 2, from: "top", to: "bottom" },
    { label: "Choose", color: "#e03c31", angle: Math.PI, from: "right", to: "left" },
  ].map((item) => ({
    ...item,
    x: cx + Math.cos(item.angle) * radiusX,
    y: cy + Math.sin(item.angle) * radiusY,
  }));

  const cardEdge = (card, edge) => {
    if (edge === "top") return { x: card.x, y: card.y - cardH / 2 - 6 * scale };
    if (edge === "bottom") return { x: card.x, y: card.y + cardH / 2 + 6 * scale };
    if (edge === "left") return { x: card.x - cardW / 2 - 8 * scale, y: card.y };
    return { x: card.x + cardW / 2 + 8 * scale, y: card.y };
  };
  const brainEdge = (edge) => {
    if (edge === "top") return { x: cx, y: cy - brainR - 12 * scale };
    if (edge === "bottom") return { x: cx, y: cy + brainR + 12 * scale };
    if (edge === "left") return { x: cx - brainR - 12 * scale, y: cy };
    return { x: cx + brainR + 12 * scale, y: cy };
  };

  cards.forEach((card) => {
    const start = cardEdge(card, card.from);
    const end = brainEdge(card.to);
    drawArrow(ctx, start.x, start.y, end.x, end.y, card.color, Math.max(2, 3 * scale));
  });

  cards.forEach(({ label, color, x, y }) => {
    roundedRect(ctx, x - cardW / 2, y - cardH / 2, cardW, cardH, 8 * scale, color);
    drawCenteredText(ctx, label, x, y + 6 * scale, 17 * scale, "#ffffff", 900);
  });
  ctx.beginPath();
  ctx.arc(cx, cy, brainR + Math.sin(t * 2) * 5 * scale, 0, Math.PI * 2);
  ctx.fillStyle = "#f3f8fb";
  ctx.fill();
  ctx.strokeStyle = "#004c97";
  ctx.lineWidth = 5 * scale;
  ctx.stroke();
  drawText(ctx, "Brain", cx - 30 * scale, cy + 6 * scale, 22 * scale, "#004c97", 900);
  movingDot(ctx, [
    { x: cx, y: cy - brainR - 52 * scale },
    { x: cx + brainR + 64 * scale, y: cy },
    { x: cx, y: cy + brainR + 52 * scale },
    { x: cx - brainR - 64 * scale, y: cy },
  ], t / 4, "#40a829");
}

function signalPlot(canvas, now) {
  const { ctx, width, height } = resizeCanvas(canvas);
  clear(ctx, width, height, "#ffffff");
  const pad = 62;
  const plotW = width - pad * 1.55;
  const plotH = height - pad * 1.55;
  const amp = state.attention / 100;
  ctx.strokeStyle = "#d6e3ea";
  ctx.lineWidth = 1;
  for (let i = 0; i < 6; i += 1) {
    const y = pad + (plotH / 5) * i;
    ctx.beginPath();
    ctx.moveTo(pad, y);
    ctx.lineTo(pad + plotW, y);
    ctx.stroke();
  }
  ctx.strokeStyle = "#102033";
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(pad, pad);
  ctx.lineTo(pad, pad + plotH);
  ctx.lineTo(pad + plotW, pad + plotH);
  ctx.stroke();
  drawText(ctx, "Signal strength", pad - 6, pad - 18, 16, "#004c97", 900);
  drawText(ctx, "Time", pad + plotW - 18, pad + plotH + 36, 16, "#004c97", 900);
  const t = now / 850;
  ctx.strokeStyle = "#009cde";
  ctx.lineWidth = 5;
  ctx.beginPath();
  for (let i = 0; i <= 240; i += 1) {
    const x = pad + (i / 240) * plotW;
    const center = (Math.sin(t * 0.8) + 1) * 0.5;
    const bump = Math.exp(-Math.pow(i / 240 - center, 2) / 0.018) * amp;
    const base = 0.18 + 0.05 * Math.sin(i / 18 + t);
    const y = pad + plotH - (base + bump * 0.68) * plotH;
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  }
  ctx.stroke();
  const dotX = pad + (((t * 40) % 240) / 240) * plotW;
  const dotY = pad + plotH - (0.22 + 0.08 * Math.sin(t)) * plotH;
  ctx.beginPath();
  ctx.arc(dotX, dotY, 7, 0, Math.PI * 2);
  ctx.fillStyle = "#e03c31";
  ctx.fill();
}

function memoryDots(canvas, now) {
  const { ctx, width, height } = resizeCanvas(canvas);
  ctx.clearRect(0, 0, width, height);
  const t = now / 900;
  ctx.globalAlpha = 0.88;
  for (let i = 0; i < 12; i += 1) {
    const x = width * (0.18 + ((i * 83) % 100) / 150);
    const y = height * (0.18 + ((i * 47) % 100) / 150);
    ctx.beginPath();
    ctx.arc(x + Math.sin(t + i) * 8, y + Math.cos(t * 0.7 + i) * 8, 5, 0, Math.PI * 2);
    ctx.fillStyle = i % 3 === 0 ? "#ffb81c" : i % 3 === 1 ? "#009cde" : "#40a829";
    ctx.fill();
  }
  ctx.globalAlpha = 1;
}

function brainNetwork(canvas, now) {
  const { ctx, width, height } = resizeCanvas(canvas);
  clear(ctx, width, height, "#ffffff");
  const t = now / 1000;
  const x0 = width * 0.08;
  const y0 = height * 0.13;
  const bw = width * 0.84;
  const bh = height * 0.70;
  const p = (x, y) => [x0 + x * bw, y0 + y * bh];
  const path = (points) => points.map(([x, y]) => ({ x: p(x, y)[0], y: p(x, y)[1] }));

  function brainShape() {
    ctx.beginPath();
    ctx.moveTo(...p(0.10, 0.58));
    ctx.bezierCurveTo(...p(0.03, 0.37), ...p(0.17, 0.16), ...p(0.38, 0.11));
    ctx.bezierCurveTo(...p(0.56, 0.03), ...p(0.81, 0.14), ...p(0.91, 0.32));
    ctx.bezierCurveTo(...p(1.00, 0.49), ...p(0.93, 0.69), ...p(0.74, 0.75));
    ctx.bezierCurveTo(...p(0.66, 0.89), ...p(0.42, 0.93), ...p(0.28, 0.78));
    ctx.bezierCurveTo(...p(0.18, 0.79), ...p(0.11, 0.70), ...p(0.10, 0.58));
    ctx.closePath();
  }

  ctx.save();
  brainShape();
  ctx.clip();
  ctx.fillStyle = "#f3f8fb";
  ctx.fillRect(x0, y0, bw, bh);

  const regions = [
    { name: "Frontal", color: "#004c97", pts: [[0.10, 0.55], [0.08, 0.35], [0.23, 0.18], [0.39, 0.17], [0.39, 0.75], [0.25, 0.78]] },
    { name: "Motor", color: "#007a33", pts: [[0.39, 0.17], [0.51, 0.13], [0.61, 0.19], [0.56, 0.77], [0.40, 0.75]] },
    { name: "Sensory", color: "#009cde", pts: [[0.59, 0.19], [0.79, 0.16], [0.91, 0.34], [0.84, 0.65], [0.58, 0.76]] },
    { name: "Hippocampus", color: "#e03c31", pts: [[0.43, 0.60], [0.55, 0.54], [0.69, 0.61], [0.62, 0.73], [0.47, 0.72]] },
    { name: "Cerebellum", color: "#775400", pts: [[0.72, 0.61], [0.90, 0.62], [0.86, 0.82], [0.68, 0.81], [0.64, 0.72]] },
  ];

  regions.forEach((region) => {
    const pts = path(region.pts);
    ctx.beginPath();
    ctx.moveTo(pts[0].x, pts[0].y);
    pts.slice(1).forEach(({ x, y }) => ctx.lineTo(x, y));
    ctx.closePath();
    ctx.fillStyle = region.color;
    ctx.globalAlpha = 0.86;
    ctx.fill();
    ctx.globalAlpha = 1;
    ctx.strokeStyle = "rgba(255, 255, 255, 0.88)";
    ctx.lineWidth = 5;
    ctx.stroke();
  });

  ctx.globalAlpha = 0.28;
  ctx.strokeStyle = "#ffffff";
  ctx.lineWidth = 3;
  for (let i = 0; i < 13; i += 1) {
    const yy = y0 + bh * (0.18 + i * 0.049);
    ctx.beginPath();
    ctx.moveTo(x0 + bw * 0.13, yy);
    ctx.bezierCurveTo(x0 + bw * 0.34, yy - bh * 0.06, x0 + bw * 0.58, yy + bh * 0.05, x0 + bw * 0.87, yy - bh * 0.04);
    ctx.stroke();
  }
  ctx.globalAlpha = 1;
  ctx.restore();

  brainShape();
  ctx.strokeStyle = "#004c97";
  ctx.lineWidth = 7;
  ctx.stroke();

  const brainStem = path([[0.50, 0.78], [0.51, 0.96], [0.43, 1.02], [0.39, 0.84]]);
  ctx.beginPath();
  ctx.moveTo(brainStem[0].x, brainStem[0].y);
  brainStem.slice(1).forEach(({ x, y }) => ctx.lineTo(x, y));
  ctx.closePath();
  ctx.fillStyle = "#8dc8e8";
  ctx.strokeStyle = "#004c97";
  ctx.lineWidth = 4;
  ctx.fill();
  ctx.stroke();

  const centers = [
    { x: p(0.25, 0.42)[0], y: p(0.25, 0.42)[1], color: "#004c97" },
    { x: p(0.50, 0.43)[0], y: p(0.50, 0.43)[1], color: "#007a33" },
    { x: p(0.73, 0.39)[0], y: p(0.73, 0.39)[1], color: "#009cde" },
    { x: p(0.55, 0.66)[0], y: p(0.55, 0.66)[1], color: "#e03c31" },
    { x: p(0.77, 0.72)[0], y: p(0.77, 0.72)[1], color: "#ffb81c" },
  ];
  for (let i = 0; i < centers.length; i += 1) {
    for (let j = i + 1; j < centers.length; j += 1) {
      ctx.strokeStyle = "rgba(0, 76, 151, 0.16)";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(centers[i].x, centers[i].y);
      ctx.lineTo(centers[j].x, centers[j].y);
      ctx.stroke();
    }
  }
  centers.forEach(({ x, y, color }, i) => {
    ctx.beginPath();
    ctx.arc(x, y, 13 + Math.sin(t * 2 + i) * 3, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.fill();
    ctx.strokeStyle = "#ffffff";
    ctx.lineWidth = 3;
    ctx.stroke();
  });
  movingDot(ctx, centers, t / 5, "#97c800");
}

function energyPlot(canvas, now) {
  const { ctx, width, height } = resizeCanvas(canvas);
  clear(ctx, width, height, "#ffffff");
  const cx = width * 0.50;
  const cy = height * 0.50;
  const t = now / 1000;
  const labels = [
    ["Oxygen", "#009cde", width * 0.22, height * 0.24, cx - 24, cy - 78],
    ["Signal", "#e03c31", width * 0.76, height * 0.22, cx + 30, cy - 80],
    ["Glucose", "#007a33", width * 0.78, height * 0.80, cx + 72, cy + 48],
    ["ATP", "#ffb81c", width * 0.22, height * 0.78, cx - 74, cy + 42],
  ];
  labels.forEach(([label, color, x, y, targetX, targetY], i) => {
    drawArrow(ctx, x, y, targetX, targetY, color, 4);
    roundedRect(ctx, x - 58, y - 24, 116, 48, 7, color);
    drawCenteredText(ctx, label, x, y + 6, 17, "#ffffff", 900);
    movingDot(ctx, [{ x, y }, { x: targetX, y: targetY }, { x: cx, y: cy }], (t + i * 0.2) / 2, color);
  });
  ctx.beginPath();
  ctx.arc(cx, cy, 78 + Math.sin(t * 2) * 6, 0, Math.PI * 2);
  ctx.fillStyle = "#f3f8fb";
  ctx.fill();
  ctx.strokeStyle = "#004c97";
  ctx.lineWidth = 5;
  ctx.stroke();
  drawText(ctx, "Active", cx - 30, cy - 4, 18, "#004c97", 900);
  drawText(ctx, "brain cell", cx - 44, cy + 22, 18, "#004c97", 900);
}

function finalNetwork(canvas, now) {
  const { ctx, width, height } = resizeCanvas(canvas);
  ctx.clearRect(0, 0, width, height);
  const t = now / 1000;
  const nodes = [
    [width * 0.22, height * 0.28, "#009cde"],
    [width * 0.72, height * 0.30, "#8dc8e8"],
    [width * 0.30, height * 0.72, "#40a829"],
    [width * 0.68, height * 0.66, "#e03c31"],
    [width * 0.50, height * 0.50, "#ffb81c"],
  ];
  ctx.lineWidth = 3;
  for (let i = 0; i < nodes.length; i += 1) {
    for (let j = i + 1; j < nodes.length; j += 1) {
      ctx.strokeStyle = "rgba(141, 200, 232, 0.16)";
      ctx.beginPath();
      ctx.moveTo(nodes[i][0], nodes[i][1]);
      ctx.lineTo(nodes[j][0], nodes[j][1]);
      ctx.stroke();
    }
  }
  nodes.forEach(([x, y, color], i) => {
    ctx.beginPath();
    ctx.arc(x, y, 42 + Math.sin(t * 2 + i) * 5, 0, Math.PI * 2);
    ctx.fillStyle = color;
    ctx.globalAlpha = 0.42;
    ctx.fill();
    ctx.globalAlpha = 1;
    ctx.strokeStyle = "rgba(255, 255, 255, 0.46)";
    ctx.lineWidth = 5;
    ctx.stroke();
  });
  movingDot(ctx, nodes.map(([x, y]) => ({ x, y })), t / 5, "#97c800");
  ctx.globalAlpha = 1;
}

function tick(now) {
  const animationMap = {
    heroSignals,
    morningReplay,
    signalPlot,
    memoryDots,
    brainNetwork,
    energyPlot,
    finalNetwork,
  };
  document.querySelectorAll("canvas[data-animation]").forEach((canvas) => {
    const name = canvas.dataset.animation;
    if (!animationMap[name]) return;
    const frame = canvas.closest(".frame");
    if (frame && !frame.classList.contains("is-active")) return;
    animationMap[name](canvas, now);
  });
  requestAnimationFrame(tick);
}

nextBtn.addEventListener("click", (event) => {
  next();
  event.currentTarget.blur();
});
prevBtn.addEventListener("click", (event) => {
  prev();
  event.currentTarget.blur();
});
notesBtn?.addEventListener("click", (event) => {
  toggleNotes();
  event.currentTarget.blur();
});
closeNotes.addEventListener("click", (event) => {
  toggleNotes(false);
  event.currentTarget.blur();
});
fullBtn.addEventListener("click", (event) => {
  toggleFullscreen();
  event.currentTarget.blur();
});
document.addEventListener("mousemove", showControls);
document.addEventListener("touchstart", showControls);

document.addEventListener("click", (event) => {
  if (event.target.closest("button, input, label, a")) return;
  next();
});

document.addEventListener("keydown", (event) => {
  if (event.key === "ArrowRight" || event.key === " " || event.key === "PageDown") {
    event.preventDefault();
    next();
  }
  if (event.key === "ArrowLeft" || event.key === "PageUp") {
    event.preventDefault();
    prev();
  }
  if (event.key === "Home") setFrame(0, 0);
  if (event.key === "End") setFrame(frames.length - 1, fragmentsFor(frames.at(-1)).length);
  if (event.key.toLowerCase() === "n") toggleNotes();
  if (event.key.toLowerCase() === "f") toggleFullscreen();
  if (event.key === "Escape") toggleNotes(false);
});

document.querySelector("#attentionSlider")?.addEventListener("input", (event) => {
  state.attention = Number(event.target.value);
});

window.addEventListener("resize", () => {
  document.querySelectorAll("canvas").forEach((canvas) => resizeCanvas(canvas));
});
document.addEventListener("visibilitychange", () => {
  if (!document.hidden) syncVideos();
});

setFrame(0, 0);
requestAnimationFrame(tick);
