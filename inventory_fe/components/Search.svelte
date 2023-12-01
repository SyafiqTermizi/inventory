<script lang="ts">
    export let searchKeyword;

    // on every keyword typed update the url search params.
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

        // I used pushState so that user can press the `back` button on the browser
        // to go to previous search result.
        window.history.pushState({ path: newUrl }, "", newUrl);
    }

    function removeSearchParams() {
        // If the user click 'clear', remove the search params and reset the `searchKeyword` store
        searchKeyword.set("");
        const newUrl =
            window.location.protocol +
            "//" +
            window.location.host +
            window.location.pathname;

        window.history.pushState({ path: newUrl }, "", newUrl);
    }
</script>

<div class="shadow" class:input-group={Boolean($searchKeyword)}>
    <input
        type="text"
        class="form-control"
        bind:value={$searchKeyword}
        placeholder="Search inventory by name"
    />
    {#if $searchKeyword}
        <button class="btn btn-outline-secondary" on:click={removeSearchParams}>
            clear
        </button>
    {/if}
</div>
