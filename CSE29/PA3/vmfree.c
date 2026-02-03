#include "vm.h"
#include "vmlib.h"

/**
 * 
 * Coalesce two adjacent free blocks into one larger free block.
 * The second block is the one that is actually adjacent to the first one.
 * 
 * Assumptions: The two blocks are adjacent and that both blocks are free.
 * 
 * @param block1 the first block to coalesce
 * @param block2 the second block to coalesce
 */
void coalesce_blocks(struct block_header* block1, struct block_header* block2) {
    block1->size_status = BLKSZ(block1) + BLKSZ(block2);
    char* footer_addr = ((char*)block1) + BLKSZ(block1) - sizeof(struct block_footer);
    struct block_footer* footer = (struct block_footer*)(footer_addr);
    footer->size = BLKSZ(block1);
}

/**
 * Returns the previous block header from the given block header.
 * If the block is at the very beginning of the heap, or if the
 * previous block is busy, returns NULL.
 * 
 * @param block the block to get the previous block from
 * @return the previous block header
 */
struct block_header* get_prev(struct block_header* block) {
    if (block == heapstart || (block->size_status & VM_PREVBUSY)) return NULL;

    char* prev_footer_addr = ((char*)block) - sizeof(struct block_footer);
    struct block_footer* prev_footer = (struct block_footer*)(prev_footer_addr);

    char* prev_block_addr = ((char*)block) - prev_footer->size;
    struct block_header* prev_block = (struct block_header*)(prev_block_addr);
    return prev_block;
}

/**
 * Frees a block of memory given a pointer to the block.
 * If the pointer is NULL or if the block isn't allocated, the function does nothing.
 * Otherwise, it marks the block as free and attempts to coalesce adjacent free blocks.
 * 
 * Assumptions: the pointer passed is a valid pointer that was returned by vmalloc.
 * 
 * @param ptr the pointer to the block to free
 */
void vmfree(void* ptr) {
    if (ptr == NULL) return;
    struct block_header* block = (struct block_header*)((char*)ptr - sizeof(struct block_header));
    if (!(block->size_status & VM_BUSY)) return;

    block->size_status &= ~VM_BUSY;
    char* footer_addr = ((char*)block) + BLKSZ(block) - sizeof(struct block_footer);
    struct block_footer* footer = (struct block_footer*)(footer_addr);
    footer->size = BLKSZ(block);

    struct block_header* next_block = (struct block_header*)(((char*)block) + BLKSZ(block));
    if (next_block->size_status != VM_ENDMARK) {
        next_block->size_status &= ~VM_PREVBUSY;
        if (!(next_block->size_status & VM_BUSY)) coalesce_blocks(block, next_block);
    }

    struct block_header* prev_block = get_prev(block);
    if (prev_block != NULL) coalesce_blocks(prev_block, block);
}
