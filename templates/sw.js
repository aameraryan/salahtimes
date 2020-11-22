
self.addEventListener('install',evt => {
    console.log("Service Worker Install");
});

self.addEventListener('activate',evt => {
    console.log("Service Worker activated");
});

self.addEventListener('fetch',evt => {
    // console.log(evt)
});
