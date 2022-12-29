<script lang="ts">
    import Api from "./services/api.js";
    import Config from "./routes/Config.svelte";
    import Setup from "./routes/Setup.svelte";

    const api = new Api();
    const promise = api.getStatus();
</script>

{#await promise then status}
    {#if status.connected}
        <Config {status} />
    {:else}
        <Setup {status} />
    {/if}
{/await}

<style>
    :root {
        font-family: "PT Sans Narrow", sans-serif;
    }
</style>