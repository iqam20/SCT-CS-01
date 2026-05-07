const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch();
    const page = await browser.newPage();

    page.on('console', msg => console.log('BROWSER LOG:', msg.text()));
    page.on('pageerror', err => console.log('BROWSER ERROR:', err));

    console.log('Navigating to local index.html...');
    await page.goto('http://127.0.0.1:3000/index.html');

    console.log('Waiting for network idle...');
    await page.waitForLoadState('networkidle');

    // Give it a bit more time for any WebGL rendering delays
    console.log('Waiting an extra 10 seconds for 3D to render...');
    await page.waitForTimeout(10000);

    await page.screenshot({ path: 'verify_final.png' });
    console.log('Screenshot saved to verify_final.png');

    await browser.close();
})();
