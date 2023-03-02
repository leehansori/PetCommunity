-- member Table Create SQL
CREATE TABLE member
(
    id              VARCHAR(50)     NOT NULL,
    pw              VARCHAR(200)    NOT NULL,
    name            VARCHAR(50)     NOT NULL,
    phone           VARCHAR(11)     NULL,
    regdate         VARCHAR(8)      NOT NULL,
    PRIMARY KEY (id)
);

COMMENT ON TABLE "member" IS '회원정보를 위한 테이블';
COMMENT ON COLUMN "member"."id" IS '이메일(id)';
COMMENT ON COLUMN "member"."pw" IS '비밀번호';
COMMENT ON COLUMN "member"."name" IS '이름';
COMMENT ON COLUMN "member"."phone" IS '핸드폰 번호';
COMMENT ON COLUMN "member"."regdate" IS '가입일자';

-- board Table Create SQL
CREATE SEQUENCE seq_board_id START 1;
COMMENT ON SEQUENCE "seq_board_id" IS '게시판id에 대한 시퀀스';

CREATE TABLE board
(
    board_id        integer         DEFAULT nextval('seq_board_id'),
    id              VARCHAR(50)     NOT NULL,
    title           VARCHAR(50)     NOT NULL,
    regdate         VARCHAR(8)      NOT NULL,
    del_yn		    BOOLEAN			NULL,
    PRIMARY KEY (board_id),
    CONSTRAINT fk_id FOREIGN KEY(id) REFERENCES "member"(id) ON DELETE CASCADE
);

COMMENT ON TABLE "board" IS '게시판을 위한 테이블';
COMMENT ON COLUMN "board"."board_id" IS '게시판id';
COMMENT ON COLUMN "board"."id" IS '이메일(id)';
COMMENT ON COLUMN "board"."title" IS '제목';
COMMENT ON COLUMN "board"."regdate" IS '등록일자';
COMMENT ON COLUMN "board"."del_yn" IS '삭제유무';

-- posting Table Create SQL
CREATE SEQUENCE seq_posting_id START 1;
COMMENT ON SEQUENCE "seq_posting_id" IS '게시글id에 대한 시퀀스';

CREATE TABLE posting
(
    posting_id      integer         DEFAULT nextval('seq_posting_id'),
    board_id        integer		  NOT NULL,
    id              VARCHAR(50)     NOT NULL,
    title           VARCHAR(50)     NOT NULL,
    CONTENT		   TEXT		  NOT NULL,
    regdate         VARCHAR(8)      NOT NULL,
    updatedate      VARCHAR(8)      NULL,
    del_yn		   boolean         NULL,
    PRIMARY KEY (posting_id),
    CONSTRAINT fk_id FOREIGN KEY(id) REFERENCES "member"(id) ON DELETE CASCADE,
    CONSTRAINT fk_board_id FOREIGN KEY(board_id) REFERENCES "board"(board_id)
);

COMMENT ON TABLE "posting" IS '게시글을 위한 테이블';
COMMENT ON COLUMN "posting"."posting_id" IS '게시글id';
COMMENT ON COLUMN "posting"."board_id" IS '게시판id';
COMMENT ON COLUMN "posting"."id" IS '이메일(id)';
COMMENT ON COLUMN "posting"."title" IS '제목';
COMMENT ON COLUMN "posting"."content" IS '내용';
COMMENT ON COLUMN "posting"."regdate" IS '등록일자';
COMMENT ON COLUMN "posting"."updatedate" IS '수정일자';
COMMENT ON COLUMN "posting"."del_yn" IS '삭제유무';


-- reply Table Create SQL
CREATE SEQUENCE seq_reply_id START 1;
COMMENT ON SEQUENCE "seq_reply_id" IS '댓글에 대한 시퀀스';

CREATE TABLE reply
(
    reply_id        integer         DEFAULT nextval('seq_reply_id'),
    posting_id      integer		  NOT NULL,
    id              VARCHAR(50)     NOT NULL,
    content		   TEXT		  NOT NULL,
    regdate         VARCHAR(8)      NOT NULL,
    updatedate      VARCHAR(8)      NULL,
    PRIMARY KEY (reply_id),
    CONSTRAINT fk_id FOREIGN KEY(id) REFERENCES "member"(id) ON DELETE CASCADE,
    CONSTRAINT fk_posting_id FOREIGN KEY(posting_id) REFERENCES "posting"(posting_id) ON DELETE CASCADE
);

COMMENT ON TABLE "reply" IS '댓글을 위한 테이블';
COMMENT ON COLUMN "reply"."reply_id" IS '댓글id';
COMMENT ON COLUMN "reply"."posting_id" IS '게시물id';
COMMENT ON COLUMN "reply"."id" IS '이메일(id)';
COMMENT ON COLUMN "reply"."content" IS '내용';
COMMENT ON COLUMN "reply"."regdate" IS '등록일자';
COMMENT ON COLUMN "reply"."updatedate" IS '수정일자';



