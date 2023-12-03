<script lang="ts">
    const headers = ["Name", "Supplier", "Availability"];
</script>

<table class="table table-hover">
    <thead>
        <tr>
            {#each headers as header}
                <th scope="col">{header}</th>
            {/each}
        </tr>
    </thead>
    <tbody>
        {#each Array(5) as _}
            <tr>
                {#each Array(headers.length) as _}
                    <td>
                        <p class="card-text placeholder-glow">
                            <span class="placeholder col-3"></span>
                        </p>
                    </td>
                {/each}
            </tr>
        {/each}
    </tbody>
</table>
