<script lang="ts">
    export let searchKeyword;

    // on every keyword typed update the url search params
    $: if ($searchKeyword) {
        const searchParams = new URLSearchParams(window.location.search);

        searchParams.set("name", $searchKeyword);

        const newUrl =
            window.location.protocol +
            "//" +
            window.location.host +
            window.location.pathname +
            "?" +
            searchParams.toString();

        window.history.pushState({ path: newUrl }, "", newUrl);
    }

    function removeSearchParams() {
        // If the user click 'clear', remove the search params and reset the store
        searchKeyword.set("");
        const newUrl =
            window.location.protocol +
            "//" +
            window.location.host +
            window.location.pathname;

        window.history.pushState({ path: newUrl }, "", newUrl);
    }
</script>

<div class:input-group={Boolean($searchKeyword)}>
    <input type="text" class="form-control" bind:value={$searchKeyword} />
    {#if $searchKeyword}
        <button class="btn btn-outline-secondary" on:click={removeSearchParams}>
            clear
        </button>
    {/if}
</div>
