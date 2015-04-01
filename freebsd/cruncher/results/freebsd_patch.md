```console
root@s4l-zfs:~/oberstet # cat patch_s4l.diff 
diff --git a/sys/amd64/amd64/uma_machdep.c b/sys/amd64/amd64/uma_machdep.c
index c0fb501..db566ae 100644
--- a/sys/amd64/amd64/uma_machdep.c
+++ b/sys/amd64/amd64/uma_machdep.c
@@ -41,7 +41,7 @@ __FBSDID("$FreeBSD$");
 #include <machine/vmparam.h>
 
 void *
-uma_small_alloc(uma_zone_t zone, int bytes, u_int8_t *flags, int wait)
+uma_small_alloc(uma_zone_t zone, vm_size_t bytes, u_int8_t *flags, int wait)
 {
    vm_page_t m;
    vm_paddr_t pa;
@@ -70,7 +70,7 @@ uma_small_alloc(uma_zone_t zone, int bytes, u_int8_t *flags, int wait)
 }
 
 void
-uma_small_free(void *mem, int size, u_int8_t flags)
+uma_small_free(void *mem, vm_size_t size, u_int8_t flags)
 {
    vm_page_t m;
    vm_paddr_t pa;
diff --git a/sys/dev/ixgbe/ix_txrx.c b/sys/dev/ixgbe/ix_txrx.c
index 536bf9f..6e86de2 100644
--- a/sys/dev/ixgbe/ix_txrx.c
+++ b/sys/dev/ixgbe/ix_txrx.c
@@ -1049,7 +1049,6 @@ ixgbe_txeof(struct tx_ring *txr)
                buf->map);
            m_freem(buf->m_head);
            buf->m_head = NULL;
-           buf->map = NULL;
        }
        buf->eop = NULL;
        ++txr->tx_avail;
@@ -1075,7 +1074,6 @@ ixgbe_txeof(struct tx_ring *txr)
                    buf->map);
                m_freem(buf->m_head);
                buf->m_head = NULL;
-               buf->map = NULL;
            }
            ++txr->tx_avail;
            buf->eop = NULL;
@@ -1318,6 +1316,7 @@ ixgbe_refresh_mbufs(struct rx_ring *rxr, int limit)
         * than replaced, there's no need to go through busdma.
         */
        if ((rxbuf->flags & IXGBE_RX_COPY) == 0) {
+           bus_dmamap_unload(rxr->ptag, rxbuf->pmap);
            /* Get the memory mapping */
            error = bus_dmamap_load_mbuf_sg(rxr->ptag,
                rxbuf->pmap, mp, seg, &nsegs, BUS_DMA_NOWAIT);
@@ -1395,8 +1394,7 @@ ixgbe_allocate_receive_buffers(struct rx_ring *rxr)
 
    for (i = 0; i < rxr->num_desc; i++, rxbuf++) {
        rxbuf = &rxr->rx_buffers[i];
-       error = bus_dmamap_create(rxr->ptag,
-           BUS_DMA_NOWAIT, &rxbuf->pmap);
+       error = bus_dmamap_create(rxr->ptag, 0, &rxbuf->pmap);
        if (error) {
            device_printf(dev, "Unable to create RX dma map\n");
            goto fail;
@@ -1715,6 +1713,7 @@ ixgbe_rx_discard(struct rx_ring *rxr, int i)
        m_free(rbuf->buf);
        rbuf->buf = NULL;
    }
+   bus_dmamap_unload(rxr->ptag, rbuf->pmap);
 
    rbuf->flags = 0;
  
diff --git a/sys/dev/nvme/nvme_private.h b/sys/dev/nvme/nvme_private.h
index fa9cb80..1214739 100644
--- a/sys/dev/nvme/nvme_private.h
+++ b/sys/dev/nvme/nvme_private.h
@@ -211,6 +211,7 @@ struct nvme_qpair {
    struct nvme_completion  *cpl;
 
    bus_dma_tag_t       dma_tag;
+   bus_dma_tag_t       dma_tag_payload;
 
    bus_dmamap_t        cmd_dma_map;
    uint64_t        cmd_bus_addr;
@@ -218,6 +219,8 @@ struct nvme_qpair {
    bus_dmamap_t        cpl_dma_map;
    uint64_t        cpl_bus_addr;
 
+   bus_addr_t      bogus_bus_addr;
+
    TAILQ_HEAD(, nvme_tracker)  free_tr;
    TAILQ_HEAD(, nvme_tracker)  outstanding_tr;
    STAILQ_HEAD(, nvme_request) queued_req;
@@ -491,6 +494,8 @@ nvme_single_map(void *arg, bus_dma_segment_t *seg, int nseg, int error)
 {
    uint64_t *bus_addr = (uint64_t *)arg;
 
+   if (error != 0)
+       printf("nvme_single_map err %d\n", error);
    *bus_addr = seg[0].ds_addr;
 }
 
diff --git a/sys/dev/nvme/nvme_qpair.c b/sys/dev/nvme/nvme_qpair.c
index e54adf7..27dd6ac 100644
--- a/sys/dev/nvme/nvme_qpair.c
+++ b/sys/dev/nvme/nvme_qpair.c
@@ -29,11 +29,18 @@ __FBSDID("$FreeBSD$");
 
 #include <sys/param.h>
 #include <sys/bus.h>
+#include <sys/memdesc.h>
 
 #include <dev/pci/pcivar.h>
 
+#include <vm/vm.h>
+#include <vm/vm_param.h>
+#include <vm/vm_page.h>
+
 #include "nvme_private.h"
 
+extern vm_page_t bogus_page;
+
 static void    _nvme_qpair_submit_request(struct nvme_qpair *qpair,
                       struct nvme_request *req);
 
@@ -294,7 +301,7 @@ nvme_qpair_construct_tracker(struct nvme_qpair *qpair, struct nvme_tracker *tr,
     uint16_t cid)
 {
 
-   bus_dmamap_create(qpair->dma_tag, 0, &tr->payload_dma_map);
+   bus_dmamap_create(qpair->dma_tag_payload, 0, &tr->payload_dma_map);
    bus_dmamap_create(qpair->dma_tag, 0, &tr->prp_dma_map);
 
    bus_dmamap_load(qpair->dma_tag, tr->prp_dma_map, tr->prp,
@@ -337,7 +344,7 @@ nvme_qpair_complete_tracker(struct nvme_qpair *qpair, struct nvme_tracker *tr,
        nvme_qpair_submit_tracker(qpair, tr);
    } else {
        if (req->type != NVME_REQUEST_NULL)
-           bus_dmamap_unload(qpair->dma_tag,
+           bus_dmamap_unload(qpair->dma_tag_payload,
                tr->payload_dma_map);
 
        nvme_free_request(req);
@@ -462,8 +469,10 @@ nvme_qpair_construct(struct nvme_qpair *qpair, uint32_t id,
     uint16_t vector, uint32_t num_entries, uint32_t num_trackers,
     struct nvme_controller *ctrlr)
 {
+   struct memdesc      md;
    struct nvme_tracker *tr;
    uint32_t        i;
+   int err;
 
    qpair->id = id;
    qpair->vector = vector;
@@ -497,11 +506,23 @@ nvme_qpair_construct(struct nvme_qpair *qpair, uint32_t id,
    mtx_init(&qpair->lock, "nvme qpair lock", NULL, MTX_DEF);
 
    /* Note: NVMe PRP format is restricted to 4-byte alignment. */
-   bus_dma_tag_create(bus_get_dma_tag(ctrlr->dev),
+   err = bus_dma_tag_create(bus_get_dma_tag(ctrlr->dev),
        4, PAGE_SIZE, BUS_SPACE_MAXADDR,
        BUS_SPACE_MAXADDR, NULL, NULL, NVME_MAX_XFER_SIZE,
        (NVME_MAX_XFER_SIZE/PAGE_SIZE)+1, PAGE_SIZE, 0,
+       NULL, NULL, &qpair->dma_tag_payload);
+   if (err != 0) {
+       device_printf(ctrlr->dev, "payload tag create failed %d\n",
+           err);
+   }
+
+   err = bus_dma_tag_create(bus_get_dma_tag(ctrlr->dev),
+       4, 0, BUS_SPACE_MAXADDR, BUS_SPACE_MAXADDR, NULL, NULL,
+       BUS_SPACE_MAXADDR, 1, BUS_SPACE_MAXSIZE, 0,
        NULL, NULL, &qpair->dma_tag);
+   if (err != 0) {
+       device_printf(ctrlr->dev, "tag create failed %d\n", err);
+   }
 
    qpair->num_cmds = 0;
    qpair->num_intr_handler_calls = 0;
@@ -513,8 +534,16 @@ nvme_qpair_construct(struct nvme_qpair *qpair, uint32_t id,
        sizeof(struct nvme_completion), M_NVME, M_ZERO,
        0, BUS_SPACE_MAXADDR, PAGE_SIZE, 0);
 
-   bus_dmamap_create(qpair->dma_tag, 0, &qpair->cmd_dma_map);
-   bus_dmamap_create(qpair->dma_tag, 0, &qpair->cpl_dma_map);
+   err = bus_dmamap_create(qpair->dma_tag, 0, &qpair->cmd_dma_map);
+   if (err != 0) {
+       device_printf(ctrlr->dev, "cmd_dma_map create failed %d\n",
+           err);
+   }
+   err = bus_dmamap_create(qpair->dma_tag, 0, &qpair->cpl_dma_map);
+   if (err != 0) {
+       device_printf(ctrlr->dev, "cpl_dma_map create failed %d\n",
+           err);
+   }
 
    bus_dmamap_load(qpair->dma_tag, qpair->cmd_dma_map,
        qpair->cmd, qpair->num_entries * sizeof(struct nvme_command),
@@ -522,6 +551,9 @@ nvme_qpair_construct(struct nvme_qpair *qpair, uint32_t id,
    bus_dmamap_load(qpair->dma_tag, qpair->cpl_dma_map,
        qpair->cpl, qpair->num_entries * sizeof(struct nvme_completion),
        nvme_single_map, &qpair->cpl_bus_addr, 0);
+   md = memdesc_paddr(VM_PAGE_TO_PHYS(bogus_page), PAGE_SIZE);
+   bus_dmamap_load_mem(qpair->dma_tag, qpair->cmd_dma_map,
+       &md, nvme_single_map, &qpair->bogus_bus_addr, 0);
 
    qpair->sq_tdbl_off = nvme_mmio_offsetof(doorbell[id].sq_tdbl);
    qpair->cq_hdbl_off = nvme_mmio_offsetof(doorbell[id].cq_hdbl);
@@ -569,6 +601,8 @@ nvme_qpair_destroy(struct nvme_qpair *qpair)
 
    if (qpair->dma_tag)
        bus_dma_tag_destroy(qpair->dma_tag);
+   if (qpair->dma_tag_payload)
+       bus_dma_tag_destroy(qpair->dma_tag_payload);
 
    if (qpair->act_tr)
        free(qpair->act_tr, M_NVME);
@@ -707,8 +741,11 @@ nvme_payload_map(void *arg, bus_dma_segment_t *seg, int nseg, int error)
     *  is responsible for detecting the error status and failing the
     *  tracker manually.
     */
-   if (error != 0)
+   if (error != 0) {
+       device_printf(tr->qpair->ctrlr->dev,
+           "nvme_payload_map err %d\n", error);
        return;
+   }
 
    /*
     * Note that we specified PAGE_SIZE for alignment and max
@@ -728,6 +765,15 @@ nvme_payload_map(void *arg, bus_dma_segment_t *seg, int nseg, int error)
                (uint64_t)seg[cur_nseg].ds_addr;
            cur_nseg++;
        }
+   } else {
+       /*
+        * Some Intel controllers write to prp2 segment even
+        * for single-segment transfer, due to a firmware
+        * defect.  As a workaround, program prp2 with the bus
+        * address of the bogus page to avoid write to zero
+        * page.
+        */
+       tr->req->cmd.prp2 = tr->qpair->bogus_bus_addr;
    }
 
    nvme_qpair_submit_tracker(tr->qpair, tr);
@@ -780,8 +826,9 @@ _nvme_qpair_submit_request(struct nvme_qpair *qpair, struct nvme_request *req)
        KASSERT(req->payload_size <= qpair->ctrlr->max_xfer_size,
            ("payload_size (%d) exceeds max_xfer_size (%d)\n",
            req->payload_size, qpair->ctrlr->max_xfer_size));
-       err = bus_dmamap_load(tr->qpair->dma_tag, tr->payload_dma_map,
-           req->u.payload, req->payload_size, nvme_payload_map, tr, 0);
+       err = bus_dmamap_load(tr->qpair->dma_tag_payload,
+           tr->payload_dma_map, req->u.payload, req->payload_size,
+           nvme_payload_map, tr, 0);
        if (err != 0)
            nvme_printf(qpair->ctrlr,
                "bus_dmamap_load returned 0x%x!\n", err);
@@ -795,7 +842,7 @@ _nvme_qpair_submit_request(struct nvme_qpair *qpair, struct nvme_request *req)
            ("bio->bio_bcount (%jd) exceeds max_xfer_size (%d)\n",
            (intmax_t)req->u.bio->bio_bcount,
            qpair->ctrlr->max_xfer_size));
-       err = bus_dmamap_load_bio(tr->qpair->dma_tag,
+       err = bus_dmamap_load_bio(tr->qpair->dma_tag_payload,
            tr->payload_dma_map, req->u.bio, nvme_payload_map, tr, 0);
        if (err != 0)
            nvme_printf(qpair->ctrlr,
diff --git a/sys/kern/kern_mbuf.c b/sys/kern/kern_mbuf.c
index 7ab6509..0648a5d 100644
--- a/sys/kern/kern_mbuf.c
+++ b/sys/kern/kern_mbuf.c
@@ -284,7 +284,7 @@ static int  mb_zinit_pack(void *, int, int);
 static void    mb_zfini_pack(void *, int);
 
 static void    mb_reclaim(void *);
-static void    *mbuf_jumbo_alloc(uma_zone_t, int, uint8_t *, int);
+static void    *mbuf_jumbo_alloc(uma_zone_t, vm_size_t, uint8_t *, int);
 
 /* Ensure that MSIZE is a power of 2. */
 CTASSERT((((MSIZE - 1) ^ MSIZE) + 1) >> 1 == MSIZE);
@@ -389,7 +389,7 @@ SYSINIT(mbuf, SI_SUB_MBUF, SI_ORDER_FIRST, mbuf_init, NULL);
  * pages.
  */
 static void *
-mbuf_jumbo_alloc(uma_zone_t zone, int bytes, uint8_t *flags, int wait)
+mbuf_jumbo_alloc(uma_zone_t zone, vm_size_t bytes, uint8_t *flags, int wait)
 {
 
    /* Inform UMA that this allocator uses kernel_map/object. */
diff --git a/sys/mips/mips/uma_machdep.c b/sys/mips/mips/uma_machdep.c
index e70dded..e47c502 100644
--- a/sys/mips/mips/uma_machdep.c
+++ b/sys/mips/mips/uma_machdep.c
@@ -41,7 +41,7 @@ __FBSDID("$FreeBSD$");
 #include <machine/vmparam.h>
 
 void *
-uma_small_alloc(uma_zone_t zone, int bytes, u_int8_t *flags, int wait)
+uma_small_alloc(uma_zone_t zone, vm_size_t bytes, u_int8_t *flags, int wait)
 {
    vm_paddr_t pa;
    vm_page_t m;
@@ -70,7 +70,7 @@ uma_small_alloc(uma_zone_t zone, int bytes, u_int8_t *flags, int wait)
 }
 
 void
-uma_small_free(void *mem, int size, u_int8_t flags)
+uma_small_free(void *mem, vm_size_t size, u_int8_t flags)
 {
    vm_page_t m;
    vm_paddr_t pa;
diff --git a/sys/powerpc/aim/uma_machdep.c b/sys/powerpc/aim/uma_machdep.c
index 4df562b..1c27e3e 100644
--- a/sys/powerpc/aim/uma_machdep.c
+++ b/sys/powerpc/aim/uma_machdep.c
@@ -50,7 +50,7 @@ SYSCTL_INT(_hw, OID_AUTO, uma_mdpages, CTLFLAG_RD, &hw_uma_mdpages, 0,
       "UMA MD pages in use");
 
 void *
-uma_small_alloc(uma_zone_t zone, int bytes, u_int8_t *flags, int wait)
+uma_small_alloc(uma_zone_t zone, vm_size_t bytes, u_int8_t *flags, int wait)
 {
    void *va;
    vm_page_t m;
@@ -82,7 +82,7 @@ uma_small_alloc(uma_zone_t zone, int bytes, u_int8_t *flags, int wait)
 }
 
 void
-uma_small_free(void *mem, int size, u_int8_t flags)
+uma_small_free(void *mem, vm_size_t size, u_int8_t flags)
 {
    vm_page_t m;
 
diff --git a/sys/sparc64/sparc64/vm_machdep.c b/sys/sparc64/sparc64/vm_machdep.c
index df184fa..df8be0b 100644
--- a/sys/sparc64/sparc64/vm_machdep.c
+++ b/sys/sparc64/sparc64/vm_machdep.c
@@ -396,7 +396,7 @@ swi_vm(void *v)
 }
 
 void *
-uma_small_alloc(uma_zone_t zone, int bytes, u_int8_t *flags, int wait)
+uma_small_alloc(uma_zone_t zone, vm_size_t bytes, u_int8_t *flags, int wait)
 {
    vm_paddr_t pa;
    vm_page_t m;
@@ -434,7 +434,7 @@ uma_small_alloc(uma_zone_t zone, int bytes, u_int8_t *flags, int wait)
 }
 
 void
-uma_small_free(void *mem, int size, u_int8_t flags)
+uma_small_free(void *mem, vm_size_t size, u_int8_t flags)
 {
    vm_page_t m;
 
diff --git a/sys/vm/uma.h b/sys/vm/uma.h
index 5012d98..df6cc5c 100644
--- a/sys/vm/uma.h
+++ b/sys/vm/uma.h
@@ -382,7 +382,8 @@ uma_zfree(uma_zone_t zone, void *item)
  * A pointer to the allocated memory or NULL on failure.
  */
 
-typedef void *(*uma_alloc)(uma_zone_t zone, int size, uint8_t *pflag, int wait);
+typedef void *(*uma_alloc)(uma_zone_t zone, vm_size_t size, uint8_t *pflag,
+    int wait);
 
 /*
  * Backend page free routines
@@ -395,7 +396,7 @@ typedef void *(*uma_alloc)(uma_zone_t zone, int size, uint8_t *pflag, int wait);
  * Returns:
  * None
  */
-typedef void (*uma_free)(void *item, int size, uint8_t pflag);
+typedef void (*uma_free)(void *item, vm_size_t size, uint8_t pflag);
 
 
 
diff --git a/sys/vm/uma_core.c b/sys/vm/uma_core.c
index 2bb6260..7556803 100644
--- a/sys/vm/uma_core.c
+++ b/sys/vm/uma_core.c
@@ -230,10 +230,10 @@ enum zfreeskip { SKIP_NONE = 0, SKIP_DTOR, SKIP_FINI };
 
 /* Prototypes.. */
 
-static void *noobj_alloc(uma_zone_t, int, uint8_t *, int);
-static void *page_alloc(uma_zone_t, int, uint8_t *, int);
-static void *startup_alloc(uma_zone_t, int, uint8_t *, int);
-static void page_free(void *, int, uint8_t);
+static void *noobj_alloc(uma_zone_t, vm_size_t, uint8_t *, int);
+static void *page_alloc(uma_zone_t, vm_size_t, uint8_t *, int);
+static void *startup_alloc(uma_zone_t, vm_size_t, uint8_t *, int);
+static void page_free(void *, vm_size_t, uint8_t);
 static uma_slab_t keg_alloc_slab(uma_keg_t, uma_zone_t, int);
 static void cache_drain(uma_zone_t);
 static void bucket_drain(uma_zone_t, uma_bucket_t);
@@ -1038,7 +1038,7 @@ out:
  * the VM is ready.
  */
 static void *
-startup_alloc(uma_zone_t zone, int bytes, uint8_t *pflag, int wait)
+startup_alloc(uma_zone_t zone, vm_size_t bytes, uint8_t *pflag, int wait)
 {
    uma_keg_t keg;
    uma_slab_t tmps;
@@ -1098,7 +1098,7 @@ startup_alloc(uma_zone_t zone, int bytes, uint8_t *pflag, int wait)
  * NULL if M_NOWAIT is set.
  */
 static void *
-page_alloc(uma_zone_t zone, int bytes, uint8_t *pflag, int wait)
+page_alloc(uma_zone_t zone, vm_size_t bytes, uint8_t *pflag, int wait)
 {
    void *p;    /* Returned page */
 
@@ -1120,7 +1120,7 @@ page_alloc(uma_zone_t zone, int bytes, uint8_t *pflag, int wait)
  * NULL if M_NOWAIT is set.
  */
 static void *
-noobj_alloc(uma_zone_t zone, int bytes, uint8_t *flags, int wait)
+noobj_alloc(uma_zone_t zone, vm_size_t bytes, uint8_t *flags, int wait)
 {
    TAILQ_HEAD(, vm_page) alloctail;
    u_long npages;
@@ -1183,7 +1183,7 @@ noobj_alloc(uma_zone_t zone, int bytes, uint8_t *flags, int wait)
  * Nothing
  */
 static void
-page_free(void *mem, int size, uint8_t flags)
+page_free(void *mem, vm_size_t size, uint8_t flags)
 {
    struct vmem *vmem;
 
@@ -3266,7 +3266,7 @@ uma_zone_exhausted_nolock(uma_zone_t zone)
 }
 
 void *
-uma_large_malloc(int size, int wait)
+uma_large_malloc(vm_size_t size, int wait)
 {
    void *mem;
    uma_slab_t slab;
diff --git a/sys/vm/uma_int.h b/sys/vm/uma_int.h
index 1ffc7d5..ad2a405 100644
--- a/sys/vm/uma_int.h
+++ b/sys/vm/uma_int.h
@@ -341,7 +341,7 @@ zone_first_keg(uma_zone_t zone)
 #ifdef _KERNEL
 /* Internal prototypes */
 static __inline uma_slab_t hash_sfind(struct uma_hash *hash, uint8_t *data);
-void *uma_large_malloc(int size, int wait);
+void *uma_large_malloc(vm_size_t size, int wait);
 void uma_large_free(uma_slab_t slab);
 
 /* Lock Macros */
@@ -424,8 +424,9 @@ vsetslab(vm_offset_t va, uma_slab_t slab)
  * if they can provide more effecient allocation functions.  This is useful
  * for using direct mapped addresses.
  */
-void *uma_small_alloc(uma_zone_t zone, int bytes, uint8_t *pflag, int wait);
-void uma_small_free(void *mem, int size, uint8_t flags);
+void *uma_small_alloc(uma_zone_t zone, vm_size_t bytes, uint8_t *pflag,
+    int wait);
+void uma_small_free(void *mem, vm_size_t size, uint8_t flags);
 #endif /* _KERNEL */
 
 #endif /* VM_UMA_INT_H */
root@s4l-zfs:~/oberstet # 
```